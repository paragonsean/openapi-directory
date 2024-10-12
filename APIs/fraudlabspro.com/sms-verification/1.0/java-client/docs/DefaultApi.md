# DefaultApi

All URIs are relative to *https://api.fraudlabspro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1VerificationResultGet**](DefaultApi.md#v1VerificationResultGet) | **GET** /v1/verification/result |  |
| [**v1VerificationSendPost**](DefaultApi.md#v1VerificationSendPost) | **POST** /v1/verification/send |  |


<a id="v1VerificationResultGet"></a>
# **v1VerificationResultGet**
> String v1VerificationResultGet(tranId, key, otp, format)



Verify that an OTP sent by the Send SMS Verification API is valid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fraudlabspro.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tranId = "tranId_example"; // String | The unique ID that was returned by the Send Verification SMS API that triggered the OTP sms.
    String key = "key_example"; // String | FraudLabs Pro API key.
    String otp = "otp_example"; // String | The OTP that was sent to the recipient’s phone.
    String format = "json"; // String | Returns the API response in json (default) or xml format.
    try {
      String result = apiInstance.v1VerificationResultGet(tranId, key, otp, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#v1VerificationResultGet");
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
| **tranId** | **String**| The unique ID that was returned by the Send Verification SMS API that triggered the OTP sms. | |
| **key** | **String**| FraudLabs Pro API key. | |
| **otp** | **String**| The OTP that was sent to the recipient’s phone. | |
| **format** | **String**| Returns the API response in json (default) or xml format. | [optional] [enum: json, xml] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get verification response |  -  |

<a id="v1VerificationSendPost"></a>
# **v1VerificationSendPost**
> String v1VerificationSendPost(tel, key, countryCode, format, mesg)



Send an SMS with verification code and a custom message for authentication purpose.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fraudlabspro.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tel = "tel_example"; // String | The recipient mobile phone number in E164 format which is a plus followed by just numbers with no spaces or parentheses.
    String key = "key_example"; // String | FraudLabs Pro API key.
    String countryCode = "countryCode_example"; // String | ISO 3166 country code for the recipient mobile phone number. If parameter is supplied, then some basic telephone number validation is done.
    String format = "json"; // String | Returns the API response in json (default) or xml format.
    String mesg = "mesg_example"; // String | The message template for the SMS. Add <otp> as placeholder for the actual OTP to be generated. Max length is 140 characters.
    try {
      String result = apiInstance.v1VerificationSendPost(tel, key, countryCode, format, mesg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#v1VerificationSendPost");
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
| **tel** | **String**| The recipient mobile phone number in E164 format which is a plus followed by just numbers with no spaces or parentheses. | |
| **key** | **String**| FraudLabs Pro API key. | |
| **countryCode** | **String**| ISO 3166 country code for the recipient mobile phone number. If parameter is supplied, then some basic telephone number validation is done. | [optional] |
| **format** | **String**| Returns the API response in json (default) or xml format. | [optional] [enum: json, xml] |
| **mesg** | **String**| The message template for the SMS. Add &lt;otp&gt; as placeholder for the actual OTP to be generated. Max length is 140 characters. | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | send verification response |  -  |

