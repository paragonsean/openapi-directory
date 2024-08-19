# AccountingApi

All URIs are relative to *https://api.fulfillment.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAccounting**](AccountingApi.md#getAccounting) | **GET** /accounting | List Order Accounting |


<a id="getAccounting"></a>
# **getAccounting**
> AccountingArrayV2 getAccounting(fromDate, toDate, hydrate, page, limit, warehouseIds, orderIds)

List Order Accounting

Retrieves accounting activity during the queried timespan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fulfillment.com/v2");
    
    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String fromDate = "fromDate_example"; // String | Orders invoice date. Date-time in ISO 8601 format for selecting orders after, or at, the specified time
    String toDate = "toDate_example"; // String | Orders invoice date. Date-time in ISO 8601 format for selecting orders before, or at, the specified time
    List<String> hydrate = Arrays.asList(); // List<String> | Adds additional information to the response, uses a CSV format for multiple values.
    Integer page = 1; // Integer | A multiplier of the number of items (limit parameter) to skip before returning results
    Integer limit = 80; // Integer | The numbers of items to return
    List<Integer> warehouseIds = Arrays.asList(); // List<Integer> | A CSV of warehouse id, '123' or '1,2,3'
    List<Integer> orderIds = Arrays.asList(); // List<Integer> | A CSV of FDC order id, '123' or '1,2,3'
    try {
      AccountingArrayV2 result = apiInstance.getAccounting(fromDate, toDate, hydrate, page, limit, warehouseIds, orderIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getAccounting");
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
| **fromDate** | **String**| Orders invoice date. Date-time in ISO 8601 format for selecting orders after, or at, the specified time | |
| **toDate** | **String**| Orders invoice date. Date-time in ISO 8601 format for selecting orders before, or at, the specified time | |
| **hydrate** | [**List&lt;String&gt;**](String.md)| Adds additional information to the response, uses a CSV format for multiple values. | [enum: items] |
| **page** | **Integer**| A multiplier of the number of items (limit parameter) to skip before returning results | [optional] [default to 1] |
| **limit** | **Integer**| The numbers of items to return | [optional] [default to 80] |
| **warehouseIds** | [**List&lt;Integer&gt;**](Integer.md)| A CSV of warehouse id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] |
| **orderIds** | [**List&lt;Integer&gt;**](Integer.md)| A CSV of FDC order id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] |

### Return type

[**AccountingArrayV2**](AccountingArrayV2.md)

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accounting |  -  |

