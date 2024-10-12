# NegotiableQuoteQuoteIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteNegotiableCartRepositoryV1SavePut**](NegotiableQuoteQuoteIdApi.md#negotiableQuoteNegotiableCartRepositoryV1SavePut) | **PUT** /V1/negotiableQuote/{quoteId} | negotiableQuote/{quoteId} |


<a id="negotiableQuoteNegotiableCartRepositoryV1SavePut"></a>
# **negotiableQuoteNegotiableCartRepositoryV1SavePut**
> ErrorResponse negotiableQuoteNegotiableCartRepositoryV1SavePut(quoteId, quoteCartRepositoryV1SavePutRequest)

negotiableQuote/{quoteId}

Save quote

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableQuoteQuoteIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableQuoteQuoteIdApi apiInstance = new NegotiableQuoteQuoteIdApi(defaultClient);
    String quoteId = "quoteId_example"; // String | 
    QuoteCartRepositoryV1SavePutRequest quoteCartRepositoryV1SavePutRequest = new QuoteCartRepositoryV1SavePutRequest(); // QuoteCartRepositoryV1SavePutRequest | 
    try {
      ErrorResponse result = apiInstance.negotiableQuoteNegotiableCartRepositoryV1SavePut(quoteId, quoteCartRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableQuoteQuoteIdApi#negotiableQuoteNegotiableCartRepositoryV1SavePut");
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
| **quoteId** | **String**|  | |
| **quoteCartRepositoryV1SavePutRequest** | [**QuoteCartRepositoryV1SavePutRequest**](QuoteCartRepositoryV1SavePutRequest.md)|  | [optional] |

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

