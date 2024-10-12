# ActivateStatementCreditOfferApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activatestatementcreditofferPost**](ActivateStatementCreditOfferApi.md#activatestatementcreditofferPost) | **POST** /activatestatementcreditoffer | Make Statement Credit Offer Available Redeemable |


<a id="activatestatementcreditofferPost"></a>
# **activatestatementcreditofferPost**
> ActivateOfferResponse activatestatementcreditofferPost(fid, userToken, offerId)

Make Statement Credit Offer Available Redeemable

This resource is used to make a statement credit offer available for redemption. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivateStatementCreditOfferApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/plo/v1");

    ActivateStatementCreditOfferApi apiInstance = new ActivateStatementCreditOfferApi(defaultClient);
    String fid = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    String userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
    String offerId = "c7dcfca7-cf35-36b0-9e67-d4f363d643e0"; // String | System-wide identifier for the campaign, not intended for end-user display.
    try {
      ActivateOfferResponse result = apiInstance.activatestatementcreditofferPost(fid, userToken, offerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivateStatementCreditOfferApi#activatestatementcreditofferPost");
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
| **fid** | **String**| Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation. | |
| **userToken** | **String**| Session identifier as returned by the UserToken resource. | |
| **offerId** | **String**| System-wide identifier for the campaign, not intended for end-user display. | |

### Return type

[**ActivateOfferResponse**](ActivateOfferResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This resource returns information about the activated offer. |  -  |
| **0** | Unexpected error |  -  |

