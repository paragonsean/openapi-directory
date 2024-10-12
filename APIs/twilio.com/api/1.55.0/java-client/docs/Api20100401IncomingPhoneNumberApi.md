# Api20100401IncomingPhoneNumberApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createIncomingPhoneNumber**](Api20100401IncomingPhoneNumberApi.md#createIncomingPhoneNumber) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json |  |
| [**deleteIncomingPhoneNumber**](Api20100401IncomingPhoneNumberApi.md#deleteIncomingPhoneNumber) | **DELETE** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json |  |
| [**fetchIncomingPhoneNumber**](Api20100401IncomingPhoneNumberApi.md#fetchIncomingPhoneNumber) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json |  |
| [**listIncomingPhoneNumber**](Api20100401IncomingPhoneNumberApi.md#listIncomingPhoneNumber) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json |  |
| [**updateIncomingPhoneNumber**](Api20100401IncomingPhoneNumberApi.md#updateIncomingPhoneNumber) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json |  |


<a id="createIncomingPhoneNumber"></a>
# **createIncomingPhoneNumber**
> ApiV2010AccountIncomingPhoneNumber createIncomingPhoneNumber(accountSid, addressSid, apiVersion, areaCode, bundleSid, emergencyAddressSid, emergencyStatus, friendlyName, identitySid, phoneNumber, smsApplicationSid, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, statusCallback, statusCallbackMethod, trunkSid, voiceApplicationSid, voiceCallerIdLookup, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceReceiveMode, voiceUrl)



Purchase a phone-number for the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IncomingPhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IncomingPhoneNumberApi apiInstance = new Api20100401IncomingPhoneNumberApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    String addressSid = "addressSid_example"; // String | The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
    String apiVersion = "apiVersion_example"; // String | The API version to use for incoming calls made to the new phone number. The default is `2010-04-01`.
    String areaCode = "areaCode_example"; // String | The desired area code for your new incoming phone number. Can be any three-digit, US or Canada area code. We will provision an available phone number within this area code for you. **You must provide an `area_code` or a `phone_number`.** (US and Canada only).
    String bundleSid = "bundleSid_example"; // String | The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
    String emergencyAddressSid = "emergencyAddressSid_example"; // String | The SID of the emergency address configuration to use for emergency calling from the new phone number.
    IncomingPhoneNumberEnumEmergencyStatus emergencyStatus = IncomingPhoneNumberEnumEmergencyStatus.fromValue("Active"); // IncomingPhoneNumberEnumEmergencyStatus | 
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the new phone number.
    String identitySid = "identitySid_example"; // String | The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations.
    String phoneNumber = "phoneNumber_example"; // String | The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
    String smsApplicationSid = "smsApplicationSid_example"; // String | The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application.
    String smsFallbackMethod = "HEAD"; // String | The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
    URI smsFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`.
    String smsMethod = "HEAD"; // String | The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`.
    URI smsUrl = new URI(); // URI | The URL we should call when the new phone number receives an incoming SMS message.
    URI statusCallback = new URI(); // URI | The URL we should call using the `status_callback_method` to send status information to your application.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
    String voiceApplicationSid = "voiceApplicationSid_example"; // String | The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
    Boolean voiceCallerIdLookup = true; // Boolean | Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
    String voiceFallbackMethod = "HEAD"; // String | The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
    URI voiceFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
    String voiceMethod = "HEAD"; // String | The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`.
    IncomingPhoneNumberEnumVoiceReceiveMode voiceReceiveMode = IncomingPhoneNumberEnumVoiceReceiveMode.fromValue("voice"); // IncomingPhoneNumberEnumVoiceReceiveMode | 
    URI voiceUrl = new URI(); // URI | The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.
    try {
      ApiV2010AccountIncomingPhoneNumber result = apiInstance.createIncomingPhoneNumber(accountSid, addressSid, apiVersion, areaCode, bundleSid, emergencyAddressSid, emergencyStatus, friendlyName, identitySid, phoneNumber, smsApplicationSid, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, statusCallback, statusCallbackMethod, trunkSid, voiceApplicationSid, voiceCallerIdLookup, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceReceiveMode, voiceUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IncomingPhoneNumberApi#createIncomingPhoneNumber");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | |
| **addressSid** | **String**| The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations. | [optional] |
| **apiVersion** | **String**| The API version to use for incoming calls made to the new phone number. The default is &#x60;2010-04-01&#x60;. | [optional] |
| **areaCode** | **String**| The desired area code for your new incoming phone number. Can be any three-digit, US or Canada area code. We will provision an available phone number within this area code for you. **You must provide an &#x60;area_code&#x60; or a &#x60;phone_number&#x60;.** (US and Canada only). | [optional] |
| **bundleSid** | **String**| The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. | [optional] |
| **emergencyAddressSid** | **String**| The SID of the emergency address configuration to use for emergency calling from the new phone number. | [optional] |
| **emergencyStatus** | **IncomingPhoneNumberEnumEmergencyStatus**|  | [optional] [enum: Active, Inactive] |
| **friendlyName** | **String**| A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the new phone number. | [optional] |
| **identitySid** | **String**| The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations. | [optional] |
| **phoneNumber** | **String**| The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234. | [optional] |
| **smsApplicationSid** | **String**| The SID of the application that should handle SMS messages sent to the new phone number. If an &#x60;sms_application_sid&#x60; is present, we ignore all of the &#x60;sms_*_url&#x60; urls and use those set on the application. | [optional] |
| **smsFallbackMethod** | **String**| The HTTP method that we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsFallbackUrl** | **URI**| The URL that we should call when an error occurs while requesting or executing the TwiML defined by &#x60;sms_url&#x60;. | [optional] |
| **smsMethod** | **String**| The HTTP method that we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsUrl** | **URI**| The URL we should call when the new phone number receives an incoming SMS message. | [optional] |
| **statusCallback** | **URI**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **trunkSid** | **String**| The SID of the Trunk we should use to handle calls to the new phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa. | [optional] |
| **voiceApplicationSid** | **String**| The SID of the application we should use to handle calls to the new phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use only those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa. | [optional] |
| **voiceCallerIdLookup** | **Boolean**| Whether to lookup the caller&#39;s name from the CNAM database and post it to your app. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional] |
| **voiceFallbackMethod** | **String**| The HTTP method that we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceFallbackUrl** | **URI**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional] |
| **voiceMethod** | **String**| The HTTP method that we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceReceiveMode** | **IncomingPhoneNumberEnumVoiceReceiveMode**|  | [optional] [enum: voice, fax] |
| **voiceUrl** | **URI**| The URL that we should call to answer a call to the new phone number. The &#x60;voice_url&#x60; will not be called if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set. | [optional] |

### Return type

[**ApiV2010AccountIncomingPhoneNumber**](ApiV2010AccountIncomingPhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteIncomingPhoneNumber"></a>
# **deleteIncomingPhoneNumber**
> deleteIncomingPhoneNumber(accountSid, sid)



Delete a phone-numbers belonging to the account used to make the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IncomingPhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IncomingPhoneNumberApi apiInstance = new Api20100401IncomingPhoneNumberApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resources to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to delete.
    try {
      apiInstance.deleteIncomingPhoneNumber(accountSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IncomingPhoneNumberApi#deleteIncomingPhoneNumber");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resources to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchIncomingPhoneNumber"></a>
# **fetchIncomingPhoneNumber**
> ApiV2010AccountIncomingPhoneNumber fetchIncomingPhoneNumber(accountSid, sid)



Fetch an incoming-phone-number belonging to the account used to make the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IncomingPhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IncomingPhoneNumberApi apiInstance = new Api20100401IncomingPhoneNumberApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to fetch.
    try {
      ApiV2010AccountIncomingPhoneNumber result = apiInstance.fetchIncomingPhoneNumber(accountSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IncomingPhoneNumberApi#fetchIncomingPhoneNumber");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to fetch. | |

### Return type

[**ApiV2010AccountIncomingPhoneNumber**](ApiV2010AccountIncomingPhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listIncomingPhoneNumber"></a>
# **listIncomingPhoneNumber**
> ListIncomingPhoneNumberResponse listIncomingPhoneNumber(accountSid, beta, friendlyName, phoneNumber, origin, pageSize, page, pageToken)



Retrieve a list of incoming-phone-numbers belonging to the account used to make the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IncomingPhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IncomingPhoneNumberApi apiInstance = new Api20100401IncomingPhoneNumberApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resources to read.
    Boolean beta = true; // Boolean | Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
    String friendlyName = "friendlyName_example"; // String | A string that identifies the IncomingPhoneNumber resources to read.
    String phoneNumber = "phoneNumber_example"; // String | The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
    String origin = "origin_example"; // String | Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListIncomingPhoneNumberResponse result = apiInstance.listIncomingPhoneNumber(accountSid, beta, friendlyName, phoneNumber, origin, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IncomingPhoneNumberApi#listIncomingPhoneNumber");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resources to read. | |
| **beta** | **Boolean**| Whether to include phone numbers new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional] |
| **friendlyName** | **String**| A string that identifies the IncomingPhoneNumber resources to read. | [optional] |
| **phoneNumber** | **String**| The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit. | [optional] |
| **origin** | **String**| Whether to include phone numbers based on their origin. Can be: &#x60;twilio&#x60; or &#x60;hosted&#x60;. By default, phone numbers of all origin are included. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListIncomingPhoneNumberResponse**](ListIncomingPhoneNumberResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateIncomingPhoneNumber"></a>
# **updateIncomingPhoneNumber**
> ApiV2010AccountIncomingPhoneNumber updateIncomingPhoneNumber(accountSid, sid, accountSid2, addressSid, apiVersion, bundleSid, emergencyAddressSid, emergencyStatus, friendlyName, identitySid, smsApplicationSid, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, statusCallback, statusCallbackMethod, trunkSid, voiceApplicationSid, voiceCallerIdLookup, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceReceiveMode, voiceUrl)



Update an incoming-phone-number instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IncomingPhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IncomingPhoneNumberApi apiInstance = new Api20100401IncomingPhoneNumberApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to update.  For more information, see [Exchanging Numbers Between Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers).
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update.
    String accountSid2 = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to update.  For more information, see [Exchanging Numbers Between Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers).
    String addressSid = "addressSid_example"; // String | The SID of the Address resource we should associate with the phone number. Some regions require addresses to meet local regulations.
    String apiVersion = "apiVersion_example"; // String | The API version to use for incoming calls made to the phone number. The default is `2010-04-01`.
    String bundleSid = "bundleSid_example"; // String | The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
    String emergencyAddressSid = "emergencyAddressSid_example"; // String | The SID of the emergency address configuration to use for emergency calling from this phone number.
    IncomingPhoneNumberEnumEmergencyStatus emergencyStatus = IncomingPhoneNumberEnumEmergencyStatus.fromValue("Active"); // IncomingPhoneNumberEnumEmergencyStatus | 
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you created to describe this phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number.
    String identitySid = "identitySid_example"; // String | The SID of the Identity resource that we should associate with the phone number. Some regions require an identity to meet local regulations.
    String smsApplicationSid = "smsApplicationSid_example"; // String | The SID of the application that should handle SMS messages sent to the number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application.
    String smsFallbackMethod = "HEAD"; // String | The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
    URI smsFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`.
    String smsMethod = "HEAD"; // String | The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`.
    URI smsUrl = new URI(); // URI | The URL we should call when the phone number receives an incoming SMS message.
    URI statusCallback = new URI(); // URI | The URL we should call using the `status_callback_method` to send status information to your application.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk we should use to handle phone calls to the phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
    String voiceApplicationSid = "voiceApplicationSid_example"; // String | The SID of the application we should use to handle phone calls to the phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
    Boolean voiceCallerIdLookup = true; // Boolean | Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
    String voiceFallbackMethod = "HEAD"; // String | The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
    URI voiceFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
    String voiceMethod = "HEAD"; // String | The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`.
    IncomingPhoneNumberEnumVoiceReceiveMode voiceReceiveMode = IncomingPhoneNumberEnumVoiceReceiveMode.fromValue("voice"); // IncomingPhoneNumberEnumVoiceReceiveMode | 
    URI voiceUrl = new URI(); // URI | The URL that we should call to answer a call to the phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.
    try {
      ApiV2010AccountIncomingPhoneNumber result = apiInstance.updateIncomingPhoneNumber(accountSid, sid, accountSid2, addressSid, apiVersion, bundleSid, emergencyAddressSid, emergencyStatus, friendlyName, identitySid, smsApplicationSid, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, statusCallback, statusCallbackMethod, trunkSid, voiceApplicationSid, voiceCallerIdLookup, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceReceiveMode, voiceUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IncomingPhoneNumberApi#updateIncomingPhoneNumber");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to update.  For more information, see [Exchanging Numbers Between Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers). | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update. | |
| **accountSid2** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to update.  For more information, see [Exchanging Numbers Between Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers). | [optional] |
| **addressSid** | **String**| The SID of the Address resource we should associate with the phone number. Some regions require addresses to meet local regulations. | [optional] |
| **apiVersion** | **String**| The API version to use for incoming calls made to the phone number. The default is &#x60;2010-04-01&#x60;. | [optional] |
| **bundleSid** | **String**| The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. | [optional] |
| **emergencyAddressSid** | **String**| The SID of the emergency address configuration to use for emergency calling from this phone number. | [optional] |
| **emergencyStatus** | **IncomingPhoneNumberEnumEmergencyStatus**|  | [optional] [enum: Active, Inactive] |
| **friendlyName** | **String**| A descriptive string that you created to describe this phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number. | [optional] |
| **identitySid** | **String**| The SID of the Identity resource that we should associate with the phone number. Some regions require an identity to meet local regulations. | [optional] |
| **smsApplicationSid** | **String**| The SID of the application that should handle SMS messages sent to the number. If an &#x60;sms_application_sid&#x60; is present, we ignore all of the &#x60;sms_*_url&#x60; urls and use those set on the application. | [optional] |
| **smsFallbackMethod** | **String**| The HTTP method that we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsFallbackUrl** | **URI**| The URL that we should call when an error occurs while requesting or executing the TwiML defined by &#x60;sms_url&#x60;. | [optional] |
| **smsMethod** | **String**| The HTTP method that we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsUrl** | **URI**| The URL we should call when the phone number receives an incoming SMS message. | [optional] |
| **statusCallback** | **URI**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **trunkSid** | **String**| The SID of the Trunk we should use to handle phone calls to the phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa. | [optional] |
| **voiceApplicationSid** | **String**| The SID of the application we should use to handle phone calls to the phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use only those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa. | [optional] |
| **voiceCallerIdLookup** | **Boolean**| Whether to lookup the caller&#39;s name from the CNAM database and post it to your app. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional] |
| **voiceFallbackMethod** | **String**| The HTTP method that we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceFallbackUrl** | **URI**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional] |
| **voiceMethod** | **String**| The HTTP method that we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceReceiveMode** | **IncomingPhoneNumberEnumVoiceReceiveMode**|  | [optional] [enum: voice, fax] |
| **voiceUrl** | **URI**| The URL that we should call to answer a call to the phone number. The &#x60;voice_url&#x60; will not be called if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set. | [optional] |

### Return type

[**ApiV2010AccountIncomingPhoneNumber**](ApiV2010AccountIncomingPhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

