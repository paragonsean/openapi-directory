# NegotiableQuoteRequestApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteNegotiableQuoteManagementV1CreatePost**](NegotiableQuoteRequestApi.md#negotiableQuoteNegotiableQuoteManagementV1CreatePost) | **POST** /V1/negotiableQuote/request | negotiableQuote/request |


<a id="negotiableQuoteNegotiableQuoteManagementV1CreatePost"></a>
# **negotiableQuoteNegotiableQuoteManagementV1CreatePost**
> Boolean negotiableQuoteNegotiableQuoteManagementV1CreatePost(negotiableQuoteNegotiableQuoteManagementV1CreatePostRequest)

negotiableQuote/request

Create a B2B quote based on a regular Magento quote. If the B2B quote requires a shipping address (for negotiation or tax calculations), add it to the regular quote before you create a B2B quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableQuoteRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableQuoteRequestApi apiInstance = new NegotiableQuoteRequestApi(defaultClient);
    NegotiableQuoteNegotiableQuoteManagementV1CreatePostRequest negotiableQuoteNegotiableQuoteManagementV1CreatePostRequest = new NegotiableQuoteNegotiableQuoteManagementV1CreatePostRequest(); // NegotiableQuoteNegotiableQuoteManagementV1CreatePostRequest | 
    try {
      Boolean result = apiInstance.negotiableQuoteNegotiableQuoteManagementV1CreatePost(negotiableQuoteNegotiableQuoteManagementV1CreatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableQuoteRequestApi#negotiableQuoteNegotiableQuoteManagementV1CreatePost");
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
| **negotiableQuoteNegotiableQuoteManagementV1CreatePostRequest** | [**NegotiableQuoteNegotiableQuoteManagementV1CreatePostRequest**](NegotiableQuoteNegotiableQuoteManagementV1CreatePostRequest.md)|  | [optional] |

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

