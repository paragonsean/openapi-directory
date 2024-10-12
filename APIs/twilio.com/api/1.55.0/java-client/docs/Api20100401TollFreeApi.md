# Api20100401TollFreeApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createIncomingPhoneNumberTollFree**](Api20100401TollFreeApi.md#createIncomingPhoneNumberTollFree) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/TollFree.json |  |
| [**listAvailablePhoneNumberTollFree**](Api20100401TollFreeApi.md#listAvailablePhoneNumberTollFree) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/TollFree.json |  |
| [**listIncomingPhoneNumberTollFree**](Api20100401TollFreeApi.md#listIncomingPhoneNumberTollFree) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/TollFree.json |  |


<a id="createIncomingPhoneNumberTollFree"></a>
# **createIncomingPhoneNumberTollFree**
> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberTollFree createIncomingPhoneNumberTollFree(accountSid, phoneNumber, addressSid, apiVersion, bundleSid, emergencyAddressSid, emergencyStatus, friendlyName, identitySid, smsApplicationSid, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, statusCallback, statusCallbackMethod, trunkSid, voiceApplicationSid, voiceCallerIdLookup, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceReceiveMode, voiceUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401TollFreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401TollFreeApi apiInstance = new Api20100401TollFreeApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    String phoneNumber = "phoneNumber_example"; // String | The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
    String addressSid = "addressSid_example"; // String | The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
    String apiVersion = "apiVersion_example"; // String | The API version to use for incoming calls made to the new phone number. The default is `2010-04-01`.
    String bundleSid = "bundleSid_example"; // String | The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
    String emergencyAddressSid = "emergencyAddressSid_example"; // String | The SID of the emergency address configuration to use for emergency calling from the new phone number.
    IncomingPhoneNumberTollFreeEnumEmergencyStatus emergencyStatus = IncomingPhoneNumberTollFreeEnumEmergencyStatus.fromValue("Active"); // IncomingPhoneNumberTollFreeEnumEmergencyStatus | 
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number.
    String identitySid = "identitySid_example"; // String | The SID of the Identity resource that we should associate with the new phone number. Some regions require an Identity to meet local regulations.
    String smsApplicationSid = "smsApplicationSid_example"; // String | The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all `sms_*_url` values and use those of the application.
    String smsFallbackMethod = "HEAD"; // String | The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
    URI smsFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`.
    String smsMethod = "HEAD"; // String | The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`.
    URI smsUrl = new URI(); // URI | The URL we should call when the new phone number receives an incoming SMS message.
    URI statusCallback = new URI(); // URI | The URL we should call using the `status_callback_method` to send status information to your application.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
    String voiceApplicationSid = "voiceApplicationSid_example"; // String | The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
    Boolean voiceCallerIdLookup = true; // Boolean | Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
    String voiceFallbackMethod = "HEAD"; // String | The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
    URI voiceFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
    String voiceMethod = "HEAD"; // String | The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`.
    IncomingPhoneNumberTollFreeEnumVoiceReceiveMode voiceReceiveMode = IncomingPhoneNumberTollFreeEnumVoiceReceiveMode.fromValue("voice"); // IncomingPhoneNumberTollFreeEnumVoiceReceiveMode | 
    URI voiceUrl = new URI(); // URI | The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.
    try {
      ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberTollFree result = apiInstance.createIncomingPhoneNumberTollFree(accountSid, phoneNumber, addressSid, apiVersion, bundleSid, emergencyAddressSid, emergencyStatus, friendlyName, identitySid, smsApplicationSid, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, statusCallback, statusCallbackMethod, trunkSid, voiceApplicationSid, voiceCallerIdLookup, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceReceiveMode, voiceUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401TollFreeApi#createIncomingPhoneNumberTollFree");
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
| **phoneNumber** | **String**| The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234. | |
| **addressSid** | **String**| The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations. | [optional] |
| **apiVersion** | **String**| The API version to use for incoming calls made to the new phone number. The default is &#x60;2010-04-01&#x60;. | [optional] |
| **bundleSid** | **String**| The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. | [optional] |
| **emergencyAddressSid** | **String**| The SID of the emergency address configuration to use for emergency calling from the new phone number. | [optional] |
| **emergencyStatus** | **IncomingPhoneNumberTollFreeEnumEmergencyStatus**|  | [optional] [enum: Active, Inactive] |
| **friendlyName** | **String**| A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number. | [optional] |
| **identitySid** | **String**| The SID of the Identity resource that we should associate with the new phone number. Some regions require an Identity to meet local regulations. | [optional] |
| **smsApplicationSid** | **String**| The SID of the application that should handle SMS messages sent to the new phone number. If an &#x60;sms_application_sid&#x60; is present, we ignore all &#x60;sms_*_url&#x60; values and use those of the application. | [optional] |
| **smsFallbackMethod** | **String**| The HTTP method that we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsFallbackUrl** | **URI**| The URL that we should call when an error occurs while requesting or executing the TwiML defined by &#x60;sms_url&#x60;. | [optional] |
| **smsMethod** | **String**| The HTTP method that we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsUrl** | **URI**| The URL we should call when the new phone number receives an incoming SMS message. | [optional] |
| **statusCallback** | **URI**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **trunkSid** | **String**| The SID of the Trunk we should use to handle calls to the new phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa. | [optional] |
| **voiceApplicationSid** | **String**| The SID of the application we should use to handle calls to the new phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa. | [optional] |
| **voiceCallerIdLookup** | **Boolean**| Whether to lookup the caller&#39;s name from the CNAM database and post it to your app. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional] |
| **voiceFallbackMethod** | **String**| The HTTP method that we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceFallbackUrl** | **URI**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional] |
| **voiceMethod** | **String**| The HTTP method that we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceReceiveMode** | **IncomingPhoneNumberTollFreeEnumVoiceReceiveMode**|  | [optional] [enum: voice, fax] |
| **voiceUrl** | **URI**| The URL that we should call to answer a call to the new phone number. The &#x60;voice_url&#x60; will not be called if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set. | [optional] |

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberTollFree**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberTollFree.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="listAvailablePhoneNumberTollFree"></a>
# **listAvailablePhoneNumberTollFree**
> ListAvailablePhoneNumberTollFreeResponse listAvailablePhoneNumberTollFree(accountSid, countryCode, areaCode, contains, smsEnabled, mmsEnabled, voiceEnabled, excludeAllAddressRequired, excludeLocalAddressRequired, excludeForeignAddressRequired, beta, nearNumber, nearLatLong, distance, inPostalCode, inRegion, inRateCenter, inLata, inLocality, faxEnabled, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401TollFreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401TollFreeApi apiInstance = new Api20100401TollFreeApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources.
    String countryCode = "countryCode_example"; // String | The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers.
    Integer areaCode = 56; // Integer | The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada.
    String contains = "contains_example"; // String | The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters.
    Boolean smsEnabled = true; // Boolean | Whether the phone numbers can receive text messages. Can be: `true` or `false`.
    Boolean mmsEnabled = true; // Boolean | Whether the phone numbers can receive MMS messages. Can be: `true` or `false`.
    Boolean voiceEnabled = true; // Boolean | Whether the phone numbers can receive calls. Can be: `true` or `false`.
    Boolean excludeAllAddressRequired = true; // Boolean | Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
    Boolean excludeLocalAddressRequired = true; // Boolean | Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
    Boolean excludeForeignAddressRequired = true; // Boolean | Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
    Boolean beta = true; // Boolean | Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
    String nearNumber = "nearNumber_example"; // String | Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada.
    String nearLatLong = "nearLatLong_example"; // String | Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada.
    Integer distance = 56; // Integer | The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada.
    String inPostalCode = "inPostalCode_example"; // String | Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada.
    String inRegion = "inRegion_example"; // String | Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada.
    String inRateCenter = "inRateCenter_example"; // String | Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada.
    String inLata = "inLata_example"; // String | Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada.
    String inLocality = "inLocality_example"; // String | Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number.
    Boolean faxEnabled = true; // Boolean | Whether the phone numbers can receive faxes. Can be: `true` or `false`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListAvailablePhoneNumberTollFreeResponse result = apiInstance.listAvailablePhoneNumberTollFree(accountSid, countryCode, areaCode, contains, smsEnabled, mmsEnabled, voiceEnabled, excludeAllAddressRequired, excludeLocalAddressRequired, excludeForeignAddressRequired, beta, nearNumber, nearLatLong, distance, inPostalCode, inRegion, inRateCenter, inLata, inLocality, faxEnabled, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401TollFreeApi#listAvailablePhoneNumberTollFree");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources. | |
| **countryCode** | **String**| The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers. | |
| **areaCode** | **Integer**| The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. | [optional] |
| **contains** | **String**| The pattern on which to match phone numbers. Valid characters are &#x60;*&#x60;, &#x60;0-9&#x60;, &#x60;a-z&#x60;, and &#x60;A-Z&#x60;. The &#x60;*&#x60; character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. | [optional] |
| **smsEnabled** | **Boolean**| Whether the phone numbers can receive text messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **mmsEnabled** | **Boolean**| Whether the phone numbers can receive MMS messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **voiceEnabled** | **Boolean**| Whether the phone numbers can receive calls. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **excludeAllAddressRequired** | **Boolean**| Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] |
| **excludeLocalAddressRequired** | **Boolean**| Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] |
| **excludeForeignAddressRequired** | **Boolean**| Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] |
| **beta** | **Boolean**| Whether to read phone numbers that are new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional] |
| **nearNumber** | **String**| Given a phone number, find a geographically close number within &#x60;distance&#x60; miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. | [optional] |
| **nearLatLong** | **String**| Given a latitude/longitude pair &#x60;lat,long&#x60; find geographically close numbers within &#x60;distance&#x60; miles. Applies to only phone numbers in the US and Canada. | [optional] |
| **distance** | **Integer**| The search radius, in miles, for a &#x60;near_&#x60; query.  Can be up to &#x60;500&#x60; and the default is &#x60;25&#x60;. Applies to only phone numbers in the US and Canada. | [optional] |
| **inPostalCode** | **String**| Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. | [optional] |
| **inRegion** | **String**| Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. | [optional] |
| **inRateCenter** | **String**| Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires &#x60;in_lata&#x60; to be set as well. Applies to only phone numbers in the US and Canada. | [optional] |
| **inLata** | **String**| Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. | [optional] |
| **inLocality** | **String**| Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. | [optional] |
| **faxEnabled** | **Boolean**| Whether the phone numbers can receive faxes. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListAvailablePhoneNumberTollFreeResponse**](ListAvailablePhoneNumberTollFreeResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listIncomingPhoneNumberTollFree"></a>
# **listIncomingPhoneNumberTollFree**
> ListIncomingPhoneNumberTollFreeResponse listIncomingPhoneNumberTollFree(accountSid, beta, friendlyName, phoneNumber, origin, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401TollFreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401TollFreeApi apiInstance = new Api20100401TollFreeApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
    Boolean beta = true; // Boolean | Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
    String friendlyName = "friendlyName_example"; // String | A string that identifies the resources to read.
    String phoneNumber = "phoneNumber_example"; // String | The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
    String origin = "origin_example"; // String | Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListIncomingPhoneNumberTollFreeResponse result = apiInstance.listIncomingPhoneNumberTollFree(accountSid, beta, friendlyName, phoneNumber, origin, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401TollFreeApi#listIncomingPhoneNumberTollFree");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read. | |
| **beta** | **Boolean**| Whether to include phone numbers new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional] |
| **friendlyName** | **String**| A string that identifies the resources to read. | [optional] |
| **phoneNumber** | **String**| The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit. | [optional] |
| **origin** | **String**| Whether to include phone numbers based on their origin. Can be: &#x60;twilio&#x60; or &#x60;hosted&#x60;. By default, phone numbers of all origin are included. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListIncomingPhoneNumberTollFreeResponse**](ListIncomingPhoneNumberTollFreeResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

