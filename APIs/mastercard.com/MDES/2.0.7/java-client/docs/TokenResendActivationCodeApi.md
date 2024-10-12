# TokenResendActivationCodeApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tokenResendactivationcodePost**](TokenResendActivationCodeApi.md#tokenResendactivationcodePost) | **POST** /token/resendactivationcode |  |


<a id="tokenResendactivationcodePost"></a>
# **tokenResendactivationcodePost**
> TokenResendActivationCodeResponseSchema tokenResendactivationcodePost(tokenResendActivationCodeRequestSchema)



Used to trigger the process of generating and sending a new Activation Code (for a specific token) to the cardholder via the requested Activation Method. When successful, a new Activation Code Expiration Date Time period will begin, and a new Activation Code will be sent to the issuer using the Activation Code Notification (ACN) pre-digitization network message. It can only be used to do this for Activation Methods that involve the external distribution of an Activation Code to the cardholder. For example, via email or SMS. It cannot be used to send a new activation code via the \&quot;Mobile Application\&quot; activation method, for instance. A new Activation Code can be sent even if the previous code has not expired. A new Activation Code can also be sent even after the previous code has expired; however, it can only be done up to 30 days after the token was created  (the number of days is subject to change at the discretion of Mastercard). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenResendActivationCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/mdes/csapi/v2");

    TokenResendActivationCodeApi apiInstance = new TokenResendActivationCodeApi(defaultClient);
    TokenResendActivationCodeRequestSchema tokenResendActivationCodeRequestSchema = new TokenResendActivationCodeRequestSchema(); // TokenResendActivationCodeRequestSchema | Contains the details of the request message.
    try {
      TokenResendActivationCodeResponseSchema result = apiInstance.tokenResendactivationcodePost(tokenResendActivationCodeRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenResendActivationCodeApi#tokenResendactivationcodePost");
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
| **tokenResendActivationCodeRequestSchema** | [**TokenResendActivationCodeRequestSchema**](TokenResendActivationCodeRequestSchema.md)| Contains the details of the request message. | [optional] |

### Return type

[**TokenResendActivationCodeResponseSchema**](TokenResendActivationCodeResponseSchema.md)

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

