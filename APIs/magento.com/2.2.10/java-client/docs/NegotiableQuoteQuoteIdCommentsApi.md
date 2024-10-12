# NegotiableQuoteQuoteIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteCommentLocatorV1GetListForQuoteGet**](NegotiableQuoteQuoteIdCommentsApi.md#negotiableQuoteCommentLocatorV1GetListForQuoteGet) | **GET** /V1/negotiableQuote/{quoteId}/comments | negotiableQuote/{quoteId}/comments |


<a id="negotiableQuoteCommentLocatorV1GetListForQuoteGet"></a>
# **negotiableQuoteCommentLocatorV1GetListForQuoteGet**
> List&lt;NegotiableQuoteDataCommentInterface&gt; negotiableQuoteCommentLocatorV1GetListForQuoteGet(quoteId)

negotiableQuote/{quoteId}/comments

Returns comments for a specified negotiable quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableQuoteQuoteIdCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableQuoteQuoteIdCommentsApi apiInstance = new NegotiableQuoteQuoteIdCommentsApi(defaultClient);
    Integer quoteId = 56; // Integer | Negotiable Quote ID.
    try {
      List<NegotiableQuoteDataCommentInterface> result = apiInstance.negotiableQuoteCommentLocatorV1GetListForQuoteGet(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableQuoteQuoteIdCommentsApi#negotiableQuoteCommentLocatorV1GetListForQuoteGet");
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
| **quoteId** | **Integer**| Negotiable Quote ID. | |

### Return type

[**List&lt;NegotiableQuoteDataCommentInterface&gt;**](NegotiableQuoteDataCommentInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

