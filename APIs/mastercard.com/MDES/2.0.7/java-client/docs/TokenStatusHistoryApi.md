# TokenStatusHistoryApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tokenStatushistoryPost**](TokenStatusHistoryApi.md#tokenStatushistoryPost) | **POST** /token/statushistory |  |


<a id="tokenStatushistoryPost"></a>
# **tokenStatushistoryPost**
> TokenStatusHistoryResponseSchema tokenStatushistoryPost(tokenStatusHistoryRequestSchema)



Used to retrieve the historical statuses and lifecycle events for a token, such as when it was initially activated, subsequently suspended or resumed, and finally deleted. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenStatusHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/mdes/csapi/v2");

    TokenStatusHistoryApi apiInstance = new TokenStatusHistoryApi(defaultClient);
    TokenStatusHistoryRequestSchema tokenStatusHistoryRequestSchema = new TokenStatusHistoryRequestSchema(); // TokenStatusHistoryRequestSchema | Contains the details of the request message.
    try {
      TokenStatusHistoryResponseSchema result = apiInstance.tokenStatushistoryPost(tokenStatusHistoryRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenStatusHistoryApi#tokenStatushistoryPost");
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
| **tokenStatusHistoryRequestSchema** | [**TokenStatusHistoryRequestSchema**](TokenStatusHistoryRequestSchema.md)| Contains the details of the request message. | [optional] |

### Return type

[**TokenStatusHistoryResponseSchema**](TokenStatusHistoryResponseSchema.md)

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

