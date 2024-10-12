# InvoicesCommentsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesInvoiceCommentRepositoryV1SavePost**](InvoicesCommentsApi.md#salesInvoiceCommentRepositoryV1SavePost) | **POST** /V1/invoices/comments | invoices/comments |


<a id="salesInvoiceCommentRepositoryV1SavePost"></a>
# **salesInvoiceCommentRepositoryV1SavePost**
> SalesDataInvoiceCommentInterface salesInvoiceCommentRepositoryV1SavePost(salesInvoiceCommentRepositoryV1SavePostRequest)

invoices/comments

Performs persist operations for a specified invoice comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    InvoicesCommentsApi apiInstance = new InvoicesCommentsApi(defaultClient);
    SalesInvoiceCommentRepositoryV1SavePostRequest salesInvoiceCommentRepositoryV1SavePostRequest = new SalesInvoiceCommentRepositoryV1SavePostRequest(); // SalesInvoiceCommentRepositoryV1SavePostRequest | 
    try {
      SalesDataInvoiceCommentInterface result = apiInstance.salesInvoiceCommentRepositoryV1SavePost(salesInvoiceCommentRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesCommentsApi#salesInvoiceCommentRepositoryV1SavePost");
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
| **salesInvoiceCommentRepositoryV1SavePostRequest** | [**SalesInvoiceCommentRepositoryV1SavePostRequest**](SalesInvoiceCommentRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**SalesDataInvoiceCommentInterface**](SalesDataInvoiceCommentInterface.md)

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

