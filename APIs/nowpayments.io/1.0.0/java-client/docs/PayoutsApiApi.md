# PayoutsApiApi

All URIs are relative to *https://api.nowpayments.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**verifyPayout**](PayoutsApiApi.md#verifyPayout) | **POST** /v1/payout/{withdrawals-id}/verify | Verify payout |


<a id="verifyPayout"></a>
# **verifyPayout**
> verifyPayout(withdrawalsId, xApiKey, verifyPayoutRequest)

Verify payout

This method is required to verify payouts by using your 2fa code.   You’ll have 10 attempts to verify the payout. If it is not verified after 10 attempts, the payout will remain in ‘creating’ status.   Payout will be processed only when it is verified.  Make sure to have your 2fa authentication enabled in your NOWPayments Account (in Account Settings).   When 2fa is disabled, the code automatically goes to your registration email.   The code sent by email is valid for one hour.  Next is a description of the required request fields:  - :batch-withdrawal-id - payout id you received in &#x60;2. Create payout&#x60; method - verification_code - 2fa code you received with your Google Auth app or via email       In order to establish an automatic verification of payouts, you should switch 2FA through the application.   There are several libraries for different frameworks aimed on generating a 2FA codes based on a secret key from your account settings.   e.g: Speakeasy for JavaScript.   We do not recommend to change any default settings.    &#x60;&#x60;&#x60; const 2faVerificationCode &#x3D; speakeasy.totp({       your_2fa_secret_key,       encoding: &#39;base32&#39;, }) &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    PayoutsApiApi apiInstance = new PayoutsApiApi(defaultClient);
    String withdrawalsId = "5000000191"; // String | 
    String xApiKey = "{{your_api_key}}"; // String | 
    VerifyPayoutRequest verifyPayoutRequest = new VerifyPayoutRequest(); // VerifyPayoutRequest | 
    try {
      apiInstance.verifyPayout(withdrawalsId, xApiKey, verifyPayoutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutsApiApi#verifyPayout");
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
| **withdrawalsId** | **String**|  | |
| **xApiKey** | **String**|  | [optional] |
| **verifyPayoutRequest** | [**VerifyPayoutRequest**](VerifyPayoutRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  -  |

