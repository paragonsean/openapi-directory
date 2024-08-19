# RetroactiveInquiryRequestApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fraudMerchantV3RetroRetroListPost**](RetroactiveInquiryRequestApi.md#fraudMerchantV3RetroRetroListPost) | **POST** /fraud/merchant/v3/retro/retro-list | Returns the summary of Retro matches for the given Acquirer Id. This resource will return the summary of Retroactive Inquiry matches for the given Acquirer ID/ICA. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry service. |


<a id="fraudMerchantV3RetroRetroListPost"></a>
# **fraudMerchantV3RetroRetroListPost**
> RetroResponseSchema fraudMerchantV3RetroRetroListPost(retroRequest)

Returns the summary of Retro matches for the given Acquirer Id. This resource will return the summary of Retroactive Inquiry matches for the given Acquirer ID/ICA. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry service.

Returns the summary of Retro matches for the given Acquirer Id. This resource will return the summary of Retroactive Inquiry matches for the given Acquirer ID/ICA. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry service. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetroactiveInquiryRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    RetroactiveInquiryRequestApi apiInstance = new RetroactiveInquiryRequestApi(defaultClient);
    RetroRequestSchema retroRequest = new RetroRequestSchema(); // RetroRequestSchema | The retro request object
    try {
      RetroResponseSchema result = apiInstance.fraudMerchantV3RetroRetroListPost(retroRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetroactiveInquiryRequestApi#fraudMerchantV3RetroRetroListPost");
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
| **retroRequest** | [**RetroRequestSchema**](RetroRequestSchema.md)| The retro request object | |

### Return type

[**RetroResponseSchema**](RetroResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retroactive request response object. |  -  |
| **0** | Unexpected error |  -  |

