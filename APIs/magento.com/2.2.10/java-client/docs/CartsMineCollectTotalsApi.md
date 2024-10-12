# CartsMineCollectTotalsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteCartTotalManagementV1CollectTotalsPut**](CartsMineCollectTotalsApi.md#quoteCartTotalManagementV1CollectTotalsPut) | **PUT** /V1/carts/mine/collect-totals | carts/mine/collect-totals |


<a id="quoteCartTotalManagementV1CollectTotalsPut"></a>
# **quoteCartTotalManagementV1CollectTotalsPut**
> QuoteDataTotalsInterface quoteCartTotalManagementV1CollectTotalsPut(quoteCartTotalManagementV1CollectTotalsPutRequest)

carts/mine/collect-totals

Set shipping/billing methods and additional data for cart and collect totals.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineCollectTotalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineCollectTotalsApi apiInstance = new CartsMineCollectTotalsApi(defaultClient);
    QuoteCartTotalManagementV1CollectTotalsPutRequest quoteCartTotalManagementV1CollectTotalsPutRequest = new QuoteCartTotalManagementV1CollectTotalsPutRequest(); // QuoteCartTotalManagementV1CollectTotalsPutRequest | 
    try {
      QuoteDataTotalsInterface result = apiInstance.quoteCartTotalManagementV1CollectTotalsPut(quoteCartTotalManagementV1CollectTotalsPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineCollectTotalsApi#quoteCartTotalManagementV1CollectTotalsPut");
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
| **quoteCartTotalManagementV1CollectTotalsPutRequest** | [**QuoteCartTotalManagementV1CollectTotalsPutRequest**](QuoteCartTotalManagementV1CollectTotalsPutRequest.md)|  | [optional] |

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

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

