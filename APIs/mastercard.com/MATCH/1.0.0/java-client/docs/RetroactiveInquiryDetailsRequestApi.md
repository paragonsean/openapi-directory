# RetroactiveInquiryDetailsRequestApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fraudMerchantV3RetroRetroInquiryDetailsPost**](RetroactiveInquiryDetailsRequestApi.md#fraudMerchantV3RetroRetroInquiryDetailsPost) | **POST** /fraud/merchant/v3/retro/retro-inquiry-details | Returns detailed information about Merchants, URLs and up to five principal owners, that have been terminated by an acquiring bank after the inquiry was made.  This MATCH resource assists acquirer&#39;s ability to consider the merchants terminated after the inquiry was made. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry Summary service. This resource can be used to obtain detailed information, such as, if a Merchant or individual has been terminated by another acquirer after an inquiry was made, the reason for termination, and the history of fraudulent or risky business practices that led to that termination. |


<a id="fraudMerchantV3RetroRetroInquiryDetailsPost"></a>
# **fraudMerchantV3RetroRetroInquiryDetailsPost**
> RetroInquiryResponseSchema fraudMerchantV3RetroRetroInquiryDetailsPost(acquirerId, retroInquiryRequest)

Returns detailed information about Merchants, URLs and up to five principal owners, that have been terminated by an acquiring bank after the inquiry was made.  This MATCH resource assists acquirer&#39;s ability to consider the merchants terminated after the inquiry was made. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry Summary service. This resource can be used to obtain detailed information, such as, if a Merchant or individual has been terminated by another acquirer after an inquiry was made, the reason for termination, and the history of fraudulent or risky business practices that led to that termination.

Returns detailed information about Merchants, URLs and up to five principal owners, that have been terminated by an acquiring bank after the inquiry was made.  This MATCH resource assists acquirer&#39;s ability to consider the merchants terminated after the inquiry was made. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry Summary service. This resource can be used to obtain detailed information, such as, if a Merchant or individual has been terminated by another acquirer after an inquiry was made, the reason for termination, and the history of fraudulent or risky business practices that led to that termination. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetroactiveInquiryDetailsRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    RetroactiveInquiryDetailsRequestApi apiInstance = new RetroactiveInquiryDetailsRequestApi(defaultClient);
    String acquirerId = "acquirerId_example"; // String | The Member ICA number which is used to validate that the application has permission to hit the MATCH database. This number must be obtained from a participating MATCH acquiring bank or entity before a developer can access the MATCH resource.
    RetroInquiryRequestSchema retroInquiryRequest = new RetroInquiryRequestSchema(); // RetroInquiryRequestSchema | The retro inquiry request object
    try {
      RetroInquiryResponseSchema result = apiInstance.fraudMerchantV3RetroRetroInquiryDetailsPost(acquirerId, retroInquiryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetroactiveInquiryDetailsRequestApi#fraudMerchantV3RetroRetroInquiryDetailsPost");
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
| **acquirerId** | **String**| The Member ICA number which is used to validate that the application has permission to hit the MATCH database. This number must be obtained from a participating MATCH acquiring bank or entity before a developer can access the MATCH resource. | |
| **retroInquiryRequest** | [**RetroInquiryRequestSchema**](RetroInquiryRequestSchema.md)| The retro inquiry request object | |

### Return type

[**RetroInquiryResponseSchema**](RetroInquiryResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retroactive inquiry response object. |  -  |
| **0** | Unexpected error |  -  |

