# VerifyV2VerificationCheckApi

All URIs are relative to *https://verify.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createVerificationCheck**](VerifyV2VerificationCheckApi.md#createVerificationCheck) | **POST** /v2/Services/{ServiceSid}/VerificationCheck |  |


<a id="createVerificationCheck"></a>
# **createVerificationCheck**
> VerifyV2ServiceVerificationCheck createVerificationCheck(serviceSid, amount, code, payee, to, verificationSid)



challenge a specific Verification Check.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2VerificationCheckApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2VerificationCheckApi apiInstance = new VerifyV2VerificationCheckApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to create the resource under.
    String amount = "amount_example"; // String | The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
    String code = "code_example"; // String | The 4-10 character string being verified.
    String payee = "payee_example"; // String | The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
    String to = "to_example"; // String | The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Either this parameter or the `verification_sid` must be specified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
    String verificationSid = "verificationSid_example"; // String | A SID that uniquely identifies the Verification Check. Either this parameter or the `to` phone number/[email](https://www.twilio.com/docs/verify/email) must be specified.
    try {
      VerifyV2ServiceVerificationCheck result = apiInstance.createVerificationCheck(serviceSid, amount, code, payee, to, verificationSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2VerificationCheckApi#createVerificationCheck");
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
| **serviceSid** | **String**| The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to create the resource under. | |
| **amount** | **String**| The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled. | [optional] |
| **code** | **String**| The 4-10 character string being verified. | [optional] |
| **payee** | **String**| The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled. | [optional] |
| **to** | **String**| The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Either this parameter or the &#x60;verification_sid&#x60; must be specified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | [optional] |
| **verificationSid** | **String**| A SID that uniquely identifies the Verification Check. Either this parameter or the &#x60;to&#x60; phone number/[email](https://www.twilio.com/docs/verify/email) must be specified. | [optional] |

### Return type

[**VerifyV2ServiceVerificationCheck**](VerifyV2ServiceVerificationCheck.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

