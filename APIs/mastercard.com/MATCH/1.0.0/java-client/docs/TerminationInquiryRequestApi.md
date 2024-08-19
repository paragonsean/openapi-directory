# TerminationInquiryRequestApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fraudMerchantV3TerminationInquiryPost**](TerminationInquiryRequestApi.md#fraudMerchantV3TerminationInquiryPost) | **POST** /fraud/merchant/v3/termination-inquiry | Returns information on merchants that have been terminated and merchants that have inquired upon. Provides the acquiring bank with information, such as, if a Merchant or individual has been terminated by another acquirer already, the reason for termination, the history of fraudulent or risky business practices that led to that termination and the inquiry that was made already on the Merchant or individual by own or another acquiring bank (if opted). |


<a id="fraudMerchantV3TerminationInquiryPost"></a>
# **fraudMerchantV3TerminationInquiryPost**
> TerminationInquirySchema fraudMerchantV3TerminationInquiryPost(pageOffset, pageLength, terminationInquiryRequest)

Returns information on merchants that have been terminated and merchants that have inquired upon. Provides the acquiring bank with information, such as, if a Merchant or individual has been terminated by another acquirer already, the reason for termination, the history of fraudulent or risky business practices that led to that termination and the inquiry that was made already on the Merchant or individual by own or another acquiring bank (if opted).

Returns information on merchants that have been terminated and merchants which have been inquired upon. MATCH can provide the acquiring bank with information, such as, if a Merchant or individual has been terminated by another acquirer already, the reason for termination, the history of fraudulent or risky business practices that led to that termination and the inquiry that was made already on the Merchant or individual by own or another acquiring bank (If opted) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminationInquiryRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    TerminationInquiryRequestApi apiInstance = new TerminationInquiryRequestApi(defaultClient);
    BigDecimal pageOffset = new BigDecimal("0"); // BigDecimal | The zero-based offset to start at. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests.
    BigDecimal pageLength = new BigDecimal("10"); // BigDecimal | The maximum number of items to retrieve within the current \"page\" of results.
    TerminationInquiryRequestSchema terminationInquiryRequest = new TerminationInquiryRequestSchema(); // TerminationInquiryRequestSchema | Body of the Termination Inquiry Request
    try {
      TerminationInquirySchema result = apiInstance.fraudMerchantV3TerminationInquiryPost(pageOffset, pageLength, terminationInquiryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminationInquiryRequestApi#fraudMerchantV3TerminationInquiryPost");
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
| **pageOffset** | **BigDecimal**| The zero-based offset to start at. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests. | |
| **pageLength** | **BigDecimal**| The maximum number of items to retrieve within the current \&quot;page\&quot; of results. | |
| **terminationInquiryRequest** | [**TerminationInquiryRequestSchema**](TerminationInquiryRequestSchema.md)| Body of the Termination Inquiry Request | |

### Return type

[**TerminationInquirySchema**](TerminationInquirySchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The termination inquiry response object. |  -  |
| **0** | Unexpected error |  -  |

