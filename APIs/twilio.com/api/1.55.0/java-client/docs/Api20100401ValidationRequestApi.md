# Api20100401ValidationRequestApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createValidationRequest**](Api20100401ValidationRequestApi.md#createValidationRequest) | **POST** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json |  |


<a id="createValidationRequest"></a>
# **createValidationRequest**
> ApiV2010AccountValidationRequest createValidationRequest(accountSid, phoneNumber, callDelay, extension, friendlyName, statusCallback, statusCallbackMethod)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ValidationRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ValidationRequestApi apiInstance = new Api20100401ValidationRequestApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the new caller ID resource.
    String phoneNumber = "phoneNumber_example"; // String | The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
    Integer callDelay = 56; // Integer | The number of seconds to delay before initiating the verification call. Can be an integer between `0` and `60`, inclusive. The default is `0`.
    String extension = "extension_example"; // String | The digits to dial after connecting the verification call.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number.
    URI statusCallback = new URI(); // URI | The URL we should call using the `status_callback_method` to send status information about the verification process to your application.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`, and the default is `POST`.
    try {
      ApiV2010AccountValidationRequest result = apiInstance.createValidationRequest(accountSid, phoneNumber, callDelay, extension, friendlyName, statusCallback, statusCallbackMethod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ValidationRequestApi#createValidationRequest");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the new caller ID resource. | |
| **phoneNumber** | **String**| The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. | |
| **callDelay** | **Integer**| The number of seconds to delay before initiating the verification call. Can be an integer between &#x60;0&#x60; and &#x60;60&#x60;, inclusive. The default is &#x60;0&#x60;. | [optional] |
| **extension** | **String**| The digits to dial after connecting the verification call. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number. | [optional] |
| **statusCallback** | **URI**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information about the verification process to your application. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;, and the default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |

### Return type

[**ApiV2010AccountValidationRequest**](ApiV2010AccountValidationRequest.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

