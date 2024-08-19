# TransactionsApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**transactionsPost**](TransactionsApi.md#transactionsPost) | **POST** /transactions |  |


<a id="transactionsPost"></a>
# **transactionsPost**
> TransactionsResponseSchema transactionsPost(transactionsRequestSchema)



Used to retrieve transactions performed by a token. It only returns transactions performed within the last 30 days, to help identify a particular token, or to identify a particular recent transaction. It is not intended to provide the full transaction history of a token or Account PAN.&lt;br&gt;&lt;br&gt;_Notes:_ The Transaction History API response is not supported for static Card on File (CoF) tokens.&lt;br&gt;If a set of tokens has been re-mapped to a new FPAN, all digital transactions will be made available before or after the FPAN has been updated. MDES does not return the value of the FPAN which was mapped to the particular token at the time of the transaction. However, MDES will return the history of all transactions performed on that particular token in the last 30 days, based on old and/or new FPAN. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/mdes/csapi/v2");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    TransactionsRequestSchema transactionsRequestSchema = new TransactionsRequestSchema(); // TransactionsRequestSchema | Contains the details of the request message.
    try {
      TransactionsResponseSchema result = apiInstance.transactionsPost(transactionsRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsPost");
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
| **transactionsRequestSchema** | [**TransactionsRequestSchema**](TransactionsRequestSchema.md)| Contains the details of the request message. | [optional] |

### Return type

[**TransactionsResponseSchema**](TransactionsResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains the details of the response message. |  -  |
| **0** | unexpected error |  -  |

