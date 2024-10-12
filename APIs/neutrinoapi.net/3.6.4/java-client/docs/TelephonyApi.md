# TelephonyApi

All URIs are relative to *https://neutrinoapi.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hLRLookup**](TelephonyApi.md#hLRLookup) | **GET** /hlr-lookup | HLR Lookup |
| [**phonePlayback**](TelephonyApi.md#phonePlayback) | **POST** /phone-playback | Phone Playback |
| [**phoneVerify**](TelephonyApi.md#phoneVerify) | **POST** /phone-verify | Phone Verify |
| [**sMSVerify**](TelephonyApi.md#sMSVerify) | **POST** /sms-verify | SMS Verify |
| [**verifySecurityCode**](TelephonyApi.md#verifySecurityCode) | **GET** /verify-security-code | Verify Security Code |


<a id="hLRLookup"></a>
# **hLRLookup**
> HLRLookupResponse hLRLookup(number, countryCode)

HLR Lookup

Connect to the global mobile cellular network and retrieve the status of a mobile device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelephonyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    TelephonyApi apiInstance = new TelephonyApi(defaultClient);
    String number = "number_example"; // String | A phone number
    String countryCode = "countryCode_example"; // String | ISO 2-letter country code, assume numbers are based in this country. <br>If not set numbers are assumed to be in international format (with or without the leading + sign)
    try {
      HLRLookupResponse result = apiInstance.hLRLookup(number, countryCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelephonyApi#hLRLookup");
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
| **number** | **String**| A phone number | |
| **countryCode** | **String**| ISO 2-letter country code, assume numbers are based in this country. &lt;br&gt;If not set numbers are assumed to be in international format (with or without the leading + sign) | [optional] |

### Return type

[**HLRLookupResponse**](HLRLookupResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="phonePlayback"></a>
# **phonePlayback**
> PhonePlaybackResponse phonePlayback(audioUrl, number, limit, limitTtl)

Phone Playback

Make an automated call to any valid phone number and playback an audio message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelephonyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    TelephonyApi apiInstance = new TelephonyApi(defaultClient);
    String audioUrl = "audioUrl_example"; // String | A URL to a valid audio file. Accepted audio formats are: <ul> <li>MP3</li> <li>WAV</li> <li>OGG</li> </ul>You can use the following MP3 URL for testing: <br>https://www.neutrinoapi.com/test-files/test1.mp3
    String number = "number_example"; // String | The phone number to call. Must be in valid international format
    Integer limit = 3; // Integer | Limit the total number of calls allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned
    Integer limitTtl = 1; // Integer | Set the TTL in number of days that the 'limit' option will remember a phone number (the default is 1 day and the maximum is 365 days)
    try {
      PhonePlaybackResponse result = apiInstance.phonePlayback(audioUrl, number, limit, limitTtl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelephonyApi#phonePlayback");
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
| **audioUrl** | **String**| A URL to a valid audio file. Accepted audio formats are: &lt;ul&gt; &lt;li&gt;MP3&lt;/li&gt; &lt;li&gt;WAV&lt;/li&gt; &lt;li&gt;OGG&lt;/li&gt; &lt;/ul&gt;You can use the following MP3 URL for testing: &lt;br&gt;https://www.neutrinoapi.com/test-files/test1.mp3 | |
| **number** | **String**| The phone number to call. Must be in valid international format | |
| **limit** | **Integer**| Limit the total number of calls allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned | [optional] [default to 3] |
| **limitTtl** | **Integer**| Set the TTL in number of days that the &#39;limit&#39; option will remember a phone number (the default is 1 day and the maximum is 365 days) | [optional] [default to 1] |

### Return type

[**PhonePlaybackResponse**](PhonePlaybackResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="phoneVerify"></a>
# **phoneVerify**
> PhoneVerifyResponse phoneVerify(number, codeLength, countryCode, languageCode, limit, limitTtl, playbackDelay, securityCode)

Phone Verify

Make an automated call to any valid phone number and playback a unique security code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelephonyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    TelephonyApi apiInstance = new TelephonyApi(defaultClient);
    String number = "number_example"; // String | The phone number to send the verification code to
    Integer codeLength = 6; // Integer | The number of digits to use in the security code (between 4 and 12)
    String countryCode = "countryCode_example"; // String | ISO 2-letter country code, assume numbers are based in this country. <br>If not set numbers are assumed to be in international format (with or without the leading + sign)
    String languageCode = "en"; // String | The language to playback the verification code in, available languages are: <ul> <li>de - German</li> <li>en - English</li> <li>es - Spanish</li> <li>fr - French</li> <li>it - Italian</li> <li>pt - Portuguese</li> <li>ru - Russian</li> </ul>
    Integer limit = 3; // Integer | Limit the total number of calls allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned
    Integer limitTtl = 1; // Integer | Set the TTL in number of days that the 'limit' option will remember a phone number (the default is 1 day and the maximum is 365 days)
    Integer playbackDelay = 800; // Integer | The delay in milliseconds between the playback of each security code
    Integer securityCode = 56; // Integer | Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code
    try {
      PhoneVerifyResponse result = apiInstance.phoneVerify(number, codeLength, countryCode, languageCode, limit, limitTtl, playbackDelay, securityCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelephonyApi#phoneVerify");
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
| **number** | **String**| The phone number to send the verification code to | |
| **codeLength** | **Integer**| The number of digits to use in the security code (between 4 and 12) | [optional] [default to 6] |
| **countryCode** | **String**| ISO 2-letter country code, assume numbers are based in this country. &lt;br&gt;If not set numbers are assumed to be in international format (with or without the leading + sign) | [optional] |
| **languageCode** | **String**| The language to playback the verification code in, available languages are: &lt;ul&gt; &lt;li&gt;de - German&lt;/li&gt; &lt;li&gt;en - English&lt;/li&gt; &lt;li&gt;es - Spanish&lt;/li&gt; &lt;li&gt;fr - French&lt;/li&gt; &lt;li&gt;it - Italian&lt;/li&gt; &lt;li&gt;pt - Portuguese&lt;/li&gt; &lt;li&gt;ru - Russian&lt;/li&gt; &lt;/ul&gt; | [optional] [default to en] |
| **limit** | **Integer**| Limit the total number of calls allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned | [optional] [default to 3] |
| **limitTtl** | **Integer**| Set the TTL in number of days that the &#39;limit&#39; option will remember a phone number (the default is 1 day and the maximum is 365 days) | [optional] [default to 1] |
| **playbackDelay** | **Integer**| The delay in milliseconds between the playback of each security code | [optional] [default to 800] |
| **securityCode** | **Integer**| Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code | [optional] |

### Return type

[**PhoneVerifyResponse**](PhoneVerifyResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="sMSVerify"></a>
# **sMSVerify**
> SMSVerifyResponse sMSVerify(number, codeLength, countryCode, languageCode, limit, limitTtl, securityCode)

SMS Verify

Send a unique security code to any mobile device via SMS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelephonyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    TelephonyApi apiInstance = new TelephonyApi(defaultClient);
    String number = "number_example"; // String | The phone number to send a verification code to
    Integer codeLength = 5; // Integer | The number of digits to use in the security code (must be between 4 and 12)
    String countryCode = "countryCode_example"; // String | ISO 2-letter country code, assume numbers are based in this country. <br>If not set numbers are assumed to be in international format (with or without the leading + sign)
    String languageCode = "en"; // String | The language to send the verification code in, available languages are: <ul> <li>de - German</li> <li>en - English</li> <li>es - Spanish</li> <li>fr - French</li> <li>it - Italian</li> <li>pt - Portuguese</li> <li>ru - Russian</li> </ul>
    Integer limit = 10; // Integer | Limit the total number of SMS allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned
    Integer limitTtl = 1; // Integer | Set the TTL in number of days that the 'limit' option will remember a phone number (the default is 1 day and the maximum is 365 days)
    Integer securityCode = 56; // Integer | Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code
    try {
      SMSVerifyResponse result = apiInstance.sMSVerify(number, codeLength, countryCode, languageCode, limit, limitTtl, securityCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelephonyApi#sMSVerify");
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
| **number** | **String**| The phone number to send a verification code to | |
| **codeLength** | **Integer**| The number of digits to use in the security code (must be between 4 and 12) | [optional] [default to 5] |
| **countryCode** | **String**| ISO 2-letter country code, assume numbers are based in this country. &lt;br&gt;If not set numbers are assumed to be in international format (with or without the leading + sign) | [optional] |
| **languageCode** | **String**| The language to send the verification code in, available languages are: &lt;ul&gt; &lt;li&gt;de - German&lt;/li&gt; &lt;li&gt;en - English&lt;/li&gt; &lt;li&gt;es - Spanish&lt;/li&gt; &lt;li&gt;fr - French&lt;/li&gt; &lt;li&gt;it - Italian&lt;/li&gt; &lt;li&gt;pt - Portuguese&lt;/li&gt; &lt;li&gt;ru - Russian&lt;/li&gt; &lt;/ul&gt; | [optional] [default to en] |
| **limit** | **Integer**| Limit the total number of SMS allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned | [optional] [default to 10] |
| **limitTtl** | **Integer**| Set the TTL in number of days that the &#39;limit&#39; option will remember a phone number (the default is 1 day and the maximum is 365 days) | [optional] [default to 1] |
| **securityCode** | **Integer**| Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code | [optional] |

### Return type

[**SMSVerifyResponse**](SMSVerifyResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="verifySecurityCode"></a>
# **verifySecurityCode**
> VerifySecurityCodeResponse verifySecurityCode(securityCode, limitBy)

Verify Security Code

Check if a security code sent via SMS Verify or Phone Verify is valid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelephonyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    TelephonyApi apiInstance = new TelephonyApi(defaultClient);
    String securityCode = "securityCode_example"; // String | The security code to verify
    String limitBy = "limitBy_example"; // String | If set then enable additional brute-force protection by limiting the number of attempts by the supplied value. This can be set to any unique identifier you would like to limit by, for example a hash of the users email, phone number or IP address. Requests to this API will be ignored after approximately 10 failed verification attempts
    try {
      VerifySecurityCodeResponse result = apiInstance.verifySecurityCode(securityCode, limitBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelephonyApi#verifySecurityCode");
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
| **securityCode** | **String**| The security code to verify | |
| **limitBy** | **String**| If set then enable additional brute-force protection by limiting the number of attempts by the supplied value. This can be set to any unique identifier you would like to limit by, for example a hash of the users email, phone number or IP address. Requests to this API will be ignored after approximately 10 failed verification attempts | [optional] |

### Return type

[**VerifySecurityCodeResponse**](VerifySecurityCodeResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

