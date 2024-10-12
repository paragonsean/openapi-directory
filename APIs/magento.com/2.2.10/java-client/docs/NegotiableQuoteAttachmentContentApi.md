# NegotiableQuoteAttachmentContentApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteAttachmentContentManagementV1GetGet**](NegotiableQuoteAttachmentContentApi.md#negotiableQuoteAttachmentContentManagementV1GetGet) | **GET** /V1/negotiableQuote/attachmentContent | negotiableQuote/attachmentContent |


<a id="negotiableQuoteAttachmentContentManagementV1GetGet"></a>
# **negotiableQuoteAttachmentContentManagementV1GetGet**
> List&lt;NegotiableQuoteDataAttachmentContentInterface&gt; negotiableQuoteAttachmentContentManagementV1GetGet(attachmentIds)

negotiableQuote/attachmentContent

Returns content for one or more files attached on the quote comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableQuoteAttachmentContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableQuoteAttachmentContentApi apiInstance = new NegotiableQuoteAttachmentContentApi(defaultClient);
    List<Integer> attachmentIds = Arrays.asList(); // List<Integer> | 
    try {
      List<NegotiableQuoteDataAttachmentContentInterface> result = apiInstance.negotiableQuoteAttachmentContentManagementV1GetGet(attachmentIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableQuoteAttachmentContentApi#negotiableQuoteAttachmentContentManagementV1GetGet");
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
| **attachmentIds** | [**List&lt;Integer&gt;**](Integer.md)|  | |

### Return type

[**List&lt;NegotiableQuoteDataAttachmentContentInterface&gt;**](NegotiableQuoteDataAttachmentContentInterface.md)

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

