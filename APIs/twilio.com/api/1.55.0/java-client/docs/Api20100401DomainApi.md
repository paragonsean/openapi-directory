# Api20100401DomainApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSipDomain**](Api20100401DomainApi.md#createSipDomain) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains.json |  |
| [**deleteSipDomain**](Api20100401DomainApi.md#deleteSipDomain) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json |  |
| [**fetchSipDomain**](Api20100401DomainApi.md#fetchSipDomain) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json |  |
| [**listSipDomain**](Api20100401DomainApi.md#listSipDomain) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains.json |  |
| [**updateSipDomain**](Api20100401DomainApi.md#updateSipDomain) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json |  |


<a id="createSipDomain"></a>
# **createSipDomain**
> ApiV2010AccountSipSipDomain createSipDomain(accountSid, domainName, byocTrunkSid, emergencyCallerSid, emergencyCallingEnabled, friendlyName, secure, sipRegistration, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceStatusCallbackMethod, voiceStatusCallbackUrl, voiceUrl)



Create a new Domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401DomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401DomainApi apiInstance = new Api20100401DomainApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    String domainName = "domainName_example"; // String | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\"-\\\" and must end with `sip.twilio.com`.
    String byocTrunkSid = "byocTrunkSid_example"; // String | The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with.
    String emergencyCallerSid = "emergencyCallerSid_example"; // String | Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call.
    Boolean emergencyCallingEnabled = true; // Boolean | Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you created to describe the resource. It can be up to 64 characters long.
    Boolean secure = true; // Boolean | Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain.
    Boolean sipRegistration = true; // Boolean | Whether to allow SIP Endpoints to register with the domain to receive calls. Can be `true` or `false`. `true` allows SIP Endpoints to register with the domain to receive calls, `false` does not.
    String voiceFallbackMethod = "HEAD"; // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
    URI voiceFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs while retrieving or executing the TwiML from `voice_url`.
    String voiceMethod = "HEAD"; // String | The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
    String voiceStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `voice_status_callback_url`. Can be: `GET` or `POST`.
    URI voiceStatusCallbackUrl = new URI(); // URI | The URL that we should call to pass status parameters (such as call ended) to your application.
    URI voiceUrl = new URI(); // URI | The URL we should when the domain receives a call.
    try {
      ApiV2010AccountSipSipDomain result = apiInstance.createSipDomain(accountSid, domainName, byocTrunkSid, emergencyCallerSid, emergencyCallingEnabled, friendlyName, secure, sipRegistration, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceStatusCallbackMethod, voiceStatusCallbackUrl, voiceUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401DomainApi#createSipDomain");
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
| **domainName** | **String**| The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\&quot;-\\\&quot; and must end with &#x60;sip.twilio.com&#x60;. | |
| **byocTrunkSid** | **String**| The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with. | [optional] |
| **emergencyCallerSid** | **String**| Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call. | [optional] |
| **emergencyCallingEnabled** | **Boolean**| Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses. | [optional] |
| **friendlyName** | **String**| A descriptive string that you created to describe the resource. It can be up to 64 characters long. | [optional] |
| **secure** | **Boolean**| Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain. | [optional] |
| **sipRegistration** | **Boolean**| Whether to allow SIP Endpoints to register with the domain to receive calls. Can be &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; allows SIP Endpoints to register with the domain to receive calls, &#x60;false&#x60; does not. | [optional] |
| **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceFallbackUrl** | **URI**| The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;voice_url&#x60;. | [optional] |
| **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceStatusCallbackUrl** | **URI**| The URL that we should call to pass status parameters (such as call ended) to your application. | [optional] |
| **voiceUrl** | **URI**| The URL we should when the domain receives a call. | [optional] |

### Return type

[**ApiV2010AccountSipSipDomain**](ApiV2010AccountSipSipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSipDomain"></a>
# **deleteSipDomain**
> deleteSipDomain(accountSid, sid)



Delete an instance of a Domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401DomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401DomainApi apiInstance = new Api20100401DomainApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the SipDomain resource to delete.
    try {
      apiInstance.deleteSipDomain(accountSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401DomainApi#deleteSipDomain");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the SipDomain resource to delete. | |

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

<a id="fetchSipDomain"></a>
# **fetchSipDomain**
> ApiV2010AccountSipSipDomain fetchSipDomain(accountSid, sid)



Fetch an instance of a Domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401DomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401DomainApi apiInstance = new Api20100401DomainApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the SipDomain resource to fetch.
    try {
      ApiV2010AccountSipSipDomain result = apiInstance.fetchSipDomain(accountSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401DomainApi#fetchSipDomain");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the SipDomain resource to fetch. | |

### Return type

[**ApiV2010AccountSipSipDomain**](ApiV2010AccountSipSipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSipDomain"></a>
# **listSipDomain**
> ListSipDomainResponse listSipDomain(accountSid, pageSize, page, pageToken)



Retrieve a list of domains belonging to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401DomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401DomainApi apiInstance = new Api20100401DomainApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSipDomainResponse result = apiInstance.listSipDomain(accountSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401DomainApi#listSipDomain");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSipDomainResponse**](ListSipDomainResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSipDomain"></a>
# **updateSipDomain**
> ApiV2010AccountSipSipDomain updateSipDomain(accountSid, sid, byocTrunkSid, domainName, emergencyCallerSid, emergencyCallingEnabled, friendlyName, secure, sipRegistration, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceStatusCallbackMethod, voiceStatusCallbackUrl, voiceUrl)



Update the attributes of a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401DomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401DomainApi apiInstance = new Api20100401DomainApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the SipDomain resource to update.
    String byocTrunkSid = "byocTrunkSid_example"; // String | The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with.
    String domainName = "domainName_example"; // String | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\"-\\\" and must end with `sip.twilio.com`.
    String emergencyCallerSid = "emergencyCallerSid_example"; // String | Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call.
    Boolean emergencyCallingEnabled = true; // Boolean | Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you created to describe the resource. It can be up to 64 characters long.
    Boolean secure = true; // Boolean | Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain.
    Boolean sipRegistration = true; // Boolean | Whether to allow SIP Endpoints to register with the domain to receive calls. Can be `true` or `false`. `true` allows SIP Endpoints to register with the domain to receive calls, `false` does not.
    String voiceFallbackMethod = "HEAD"; // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
    URI voiceFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.
    String voiceMethod = "HEAD"; // String | The HTTP method we should use to call `voice_url`
    String voiceStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `voice_status_callback_url`. Can be: `GET` or `POST`.
    URI voiceStatusCallbackUrl = new URI(); // URI | The URL that we should call to pass status parameters (such as call ended) to your application.
    URI voiceUrl = new URI(); // URI | The URL we should call when the domain receives a call.
    try {
      ApiV2010AccountSipSipDomain result = apiInstance.updateSipDomain(accountSid, sid, byocTrunkSid, domainName, emergencyCallerSid, emergencyCallingEnabled, friendlyName, secure, sipRegistration, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceStatusCallbackMethod, voiceStatusCallbackUrl, voiceUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401DomainApi#updateSipDomain");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the SipDomain resource to update. | |
| **byocTrunkSid** | **String**| The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with. | [optional] |
| **domainName** | **String**| The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\&quot;-\\\&quot; and must end with &#x60;sip.twilio.com&#x60;. | [optional] |
| **emergencyCallerSid** | **String**| Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call. | [optional] |
| **emergencyCallingEnabled** | **Boolean**| Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses. | [optional] |
| **friendlyName** | **String**| A descriptive string that you created to describe the resource. It can be up to 64 characters long. | [optional] |
| **secure** | **Boolean**| Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain. | [optional] |
| **sipRegistration** | **Boolean**| Whether to allow SIP Endpoints to register with the domain to receive calls. Can be &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; allows SIP Endpoints to register with the domain to receive calls, &#x60;false&#x60; does not. | [optional] |
| **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceFallbackUrl** | **URI**| The URL that we should call when an error occurs while retrieving or executing the TwiML requested by &#x60;voice_url&#x60;. | [optional] |
| **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60; | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceStatusCallbackUrl** | **URI**| The URL that we should call to pass status parameters (such as call ended) to your application. | [optional] |
| **voiceUrl** | **URI**| The URL we should call when the domain receives a call. | [optional] |

### Return type

[**ApiV2010AccountSipSipDomain**](ApiV2010AccountSipSipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

