# VoucherHistoryApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**voucherHistoryGetVoucherHistory**](VoucherHistoryApi.md#voucherHistoryGetVoucherHistory) | **GET** /api/v2/VoucherHistory | Gets voucher history data |


<a id="voucherHistoryGetVoucherHistory"></a>
# **voucherHistoryGetVoucherHistory**
> APIPagedResponseDealerDBModelsVoucherHistory voucherHistoryGetVoucherHistory(voucherCode, changedBefore, changedAfter, limit, offset)

Gets voucher history data

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoucherHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    VoucherHistoryApi apiInstance = new VoucherHistoryApi(defaultClient);
    String voucherCode = "voucherCode_example"; // String | Optional. Filter history data by Voucher Code.
    OffsetDateTime changedBefore = OffsetDateTime.now(); // OffsetDateTime | Optional. Filter history data where changes occured before provided date.
    OffsetDateTime changedAfter = OffsetDateTime.now(); // OffsetDateTime | Optional. Filter history data where changes occured after provided date.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseDealerDBModelsVoucherHistory result = apiInstance.voucherHistoryGetVoucherHistory(voucherCode, changedBefore, changedAfter, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoucherHistoryApi#voucherHistoryGetVoucherHistory");
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
| **voucherCode** | **String**| Optional. Filter history data by Voucher Code. | [optional] |
| **changedBefore** | **OffsetDateTime**| Optional. Filter history data where changes occured before provided date. | [optional] |
| **changedAfter** | **OffsetDateTime**| Optional. Filter history data where changes occured after provided date. | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseDealerDBModelsVoucherHistory**](APIPagedResponseDealerDBModelsVoucherHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

