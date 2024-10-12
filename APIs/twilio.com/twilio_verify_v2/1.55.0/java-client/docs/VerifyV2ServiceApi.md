# VerifyV2ServiceApi

All URIs are relative to *https://verify.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createService**](VerifyV2ServiceApi.md#createService) | **POST** /v2/Services |  |
| [**deleteService**](VerifyV2ServiceApi.md#deleteService) | **DELETE** /v2/Services/{Sid} |  |
| [**fetchService**](VerifyV2ServiceApi.md#fetchService) | **GET** /v2/Services/{Sid} |  |
| [**listService**](VerifyV2ServiceApi.md#listService) | **GET** /v2/Services |  |
| [**updateService**](VerifyV2ServiceApi.md#updateService) | **POST** /v2/Services/{Sid} |  |


<a id="createService"></a>
# **createService**
> VerifyV2Service createService(friendlyName, codeLength, customCodeEnabled, defaultTemplateSid, doNotShareWarningEnabled, dtmfInputRequired, lookupEnabled, psd2Enabled, pushApnCredentialSid, pushFcmCredentialSid, pushIncludeDate, skipSmsToLandlines, totpCodeLength, totpIssuer, totpSkew, totpTimeStep, ttsName, verifyEventSubscriptionEnabled)



Create a new Verification Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2ServiceApi apiInstance = new VerifyV2ServiceApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.**
    Integer codeLength = 56; // Integer | The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.
    Boolean customCodeEnabled = true; // Boolean | Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers.
    String defaultTemplateSid = "defaultTemplateSid_example"; // String | The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
    Boolean doNotShareWarningEnabled = true; // Boolean | Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to SMS. Example SMS body: `Your AppName verification code is: 1234. Don’t share this code with anyone; our employees will never ask for the code`
    Boolean dtmfInputRequired = true; // Boolean | Whether to ask the user to press a number before delivering the verify code in a phone call.
    Boolean lookupEnabled = true; // Boolean | Whether to perform a lookup with each verification started and return info about the phone number.
    Boolean psd2Enabled = true; // Boolean | Whether to pass PSD2 transaction parameters when starting a verification.
    String pushApnCredentialSid = "pushApnCredentialSid_example"; // String | Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
    String pushFcmCredentialSid = "pushFcmCredentialSid_example"; // String | Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
    Boolean pushIncludeDate = true; // Boolean | Optional configuration for the Push factors. If true, include the date in the Challenge's response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter. This timestamp value is the same one as the one found in `date_created`, please use that one instead.
    Boolean skipSmsToLandlines = true; // Boolean | Whether to skip sending SMS verifications to landlines. Requires `lookup_enabled`.
    Integer totpCodeLength = 56; // Integer | Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6
    String totpIssuer = "totpIssuer_example"; // String | Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided.
    Integer totpSkew = 56; // Integer | Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
    Integer totpTimeStep = 56; // Integer | Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds
    String ttsName = "ttsName_example"; // String | The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.
    Boolean verifyEventSubscriptionEnabled = true; // Boolean | Whether to allow verifications from the service to reach the stream-events sinks if configured
    try {
      VerifyV2Service result = apiInstance.createService(friendlyName, codeLength, customCodeEnabled, defaultTemplateSid, doNotShareWarningEnabled, dtmfInputRequired, lookupEnabled, psd2Enabled, pushApnCredentialSid, pushFcmCredentialSid, pushIncludeDate, skipSmsToLandlines, totpCodeLength, totpIssuer, totpSkew, totpTimeStep, ttsName, verifyEventSubscriptionEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2ServiceApi#createService");
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
| **friendlyName** | **String**| A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.** | |
| **codeLength** | **Integer**| The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive. | [optional] |
| **customCodeEnabled** | **Boolean**| Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers. | [optional] |
| **defaultTemplateSid** | **String**| The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only. | [optional] |
| **doNotShareWarningEnabled** | **Boolean**| Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to SMS. Example SMS body: &#x60;Your AppName verification code is: 1234. Don’t share this code with anyone; our employees will never ask for the code&#x60; | [optional] |
| **dtmfInputRequired** | **Boolean**| Whether to ask the user to press a number before delivering the verify code in a phone call. | [optional] |
| **lookupEnabled** | **Boolean**| Whether to perform a lookup with each verification started and return info about the phone number. | [optional] |
| **psd2Enabled** | **Boolean**| Whether to pass PSD2 transaction parameters when starting a verification. | [optional] |
| **pushApnCredentialSid** | **String**| Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource) | [optional] |
| **pushFcmCredentialSid** | **String**| Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource) | [optional] |
| **pushIncludeDate** | **Boolean**| Optional configuration for the Push factors. If true, include the date in the Challenge&#39;s response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter. This timestamp value is the same one as the one found in &#x60;date_created&#x60;, please use that one instead. | [optional] |
| **skipSmsToLandlines** | **Boolean**| Whether to skip sending SMS verifications to landlines. Requires &#x60;lookup_enabled&#x60;. | [optional] |
| **totpCodeLength** | **Integer**| Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6 | [optional] |
| **totpIssuer** | **String**| Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided. | [optional] |
| **totpSkew** | **Integer**| Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1 | [optional] |
| **totpTimeStep** | **Integer**| Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds | [optional] |
| **ttsName** | **String**| The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages. | [optional] |
| **verifyEventSubscriptionEnabled** | **Boolean**| Whether to allow verifications from the service to reach the stream-events sinks if configured | [optional] |

### Return type

[**VerifyV2Service**](VerifyV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteService"></a>
# **deleteService**
> deleteService(sid)



Delete a specific Verification Service Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2ServiceApi apiInstance = new VerifyV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Verification Service resource to delete.
    try {
      apiInstance.deleteService(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2ServiceApi#deleteService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Verification Service resource to delete. | |

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

<a id="fetchService"></a>
# **fetchService**
> VerifyV2Service fetchService(sid)



Fetch specific Verification Service Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2ServiceApi apiInstance = new VerifyV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Verification Service resource to fetch.
    try {
      VerifyV2Service result = apiInstance.fetchService(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2ServiceApi#fetchService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Verification Service resource to fetch. | |

### Return type

[**VerifyV2Service**](VerifyV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listService"></a>
# **listService**
> ListServiceResponse listService(pageSize, page, pageToken)



Retrieve a list of all Verification Services for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2ServiceApi apiInstance = new VerifyV2ServiceApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceResponse result = apiInstance.listService(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2ServiceApi#listService");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateService"></a>
# **updateService**
> VerifyV2Service updateService(sid, codeLength, customCodeEnabled, defaultTemplateSid, doNotShareWarningEnabled, dtmfInputRequired, friendlyName, lookupEnabled, psd2Enabled, pushApnCredentialSid, pushFcmCredentialSid, pushIncludeDate, skipSmsToLandlines, totpCodeLength, totpIssuer, totpSkew, totpTimeStep, ttsName, verifyEventSubscriptionEnabled)



Update a specific Verification Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2ServiceApi apiInstance = new VerifyV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to update.
    Integer codeLength = 56; // Integer | The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.
    Boolean customCodeEnabled = true; // Boolean | Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers.
    String defaultTemplateSid = "defaultTemplateSid_example"; // String | The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only.
    Boolean doNotShareWarningEnabled = true; // Boolean | Whether to add a privacy warning at the end of an SMS. **Disabled by default and applies only for SMS.**
    Boolean dtmfInputRequired = true; // Boolean | Whether to ask the user to press a number before delivering the verify code in a phone call.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.**
    Boolean lookupEnabled = true; // Boolean | Whether to perform a lookup with each verification started and return info about the phone number.
    Boolean psd2Enabled = true; // Boolean | Whether to pass PSD2 transaction parameters when starting a verification.
    String pushApnCredentialSid = "pushApnCredentialSid_example"; // String | Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
    String pushFcmCredentialSid = "pushFcmCredentialSid_example"; // String | Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource)
    Boolean pushIncludeDate = true; // Boolean | Optional configuration for the Push factors. If true, include the date in the Challenge's response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter.
    Boolean skipSmsToLandlines = true; // Boolean | Whether to skip sending SMS verifications to landlines. Requires `lookup_enabled`.
    Integer totpCodeLength = 56; // Integer | Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6
    String totpIssuer = "totpIssuer_example"; // String | Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI.
    Integer totpSkew = 56; // Integer | Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1
    Integer totpTimeStep = 56; // Integer | Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds
    String ttsName = "ttsName_example"; // String | The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.
    Boolean verifyEventSubscriptionEnabled = true; // Boolean | Whether to allow verifications from the service to reach the stream-events sinks if configured
    try {
      VerifyV2Service result = apiInstance.updateService(sid, codeLength, customCodeEnabled, defaultTemplateSid, doNotShareWarningEnabled, dtmfInputRequired, friendlyName, lookupEnabled, psd2Enabled, pushApnCredentialSid, pushFcmCredentialSid, pushIncludeDate, skipSmsToLandlines, totpCodeLength, totpIssuer, totpSkew, totpTimeStep, ttsName, verifyEventSubscriptionEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2ServiceApi#updateService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to update. | |
| **codeLength** | **Integer**| The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive. | [optional] |
| **customCodeEnabled** | **Boolean**| Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers. | [optional] |
| **defaultTemplateSid** | **String**| The default message [template](https://www.twilio.com/docs/verify/api/templates). Will be used for all SMS verifications unless explicitly overriden. SMS channel only. | [optional] |
| **doNotShareWarningEnabled** | **Boolean**| Whether to add a privacy warning at the end of an SMS. **Disabled by default and applies only for SMS.** | [optional] |
| **dtmfInputRequired** | **Boolean**| Whether to ask the user to press a number before delivering the verify code in a phone call. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.** | [optional] |
| **lookupEnabled** | **Boolean**| Whether to perform a lookup with each verification started and return info about the phone number. | [optional] |
| **psd2Enabled** | **Boolean**| Whether to pass PSD2 transaction parameters when starting a verification. | [optional] |
| **pushApnCredentialSid** | **String**| Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource) | [optional] |
| **pushFcmCredentialSid** | **String**| Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](https://www.twilio.com/docs/notify/api/credential-resource) | [optional] |
| **pushIncludeDate** | **Boolean**| Optional configuration for the Push factors. If true, include the date in the Challenge&#39;s response. Otherwise, the date is omitted from the response. See [Challenge](https://www.twilio.com/docs/verify/api/challenge) resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter. | [optional] |
| **skipSmsToLandlines** | **Boolean**| Whether to skip sending SMS verifications to landlines. Requires &#x60;lookup_enabled&#x60;. | [optional] |
| **totpCodeLength** | **Integer**| Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6 | [optional] |
| **totpIssuer** | **String**| Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI. | [optional] |
| **totpSkew** | **Integer**| Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1 | [optional] |
| **totpTimeStep** | **Integer**| Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds | [optional] |
| **ttsName** | **String**| The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages. | [optional] |
| **verifyEventSubscriptionEnabled** | **Boolean**| Whether to allow verifications from the service to reach the stream-events sinks if configured | [optional] |

### Return type

[**VerifyV2Service**](VerifyV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

