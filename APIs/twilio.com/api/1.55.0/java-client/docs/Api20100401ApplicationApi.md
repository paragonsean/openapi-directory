# Api20100401ApplicationApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApplication**](Api20100401ApplicationApi.md#createApplication) | **POST** /2010-04-01/Accounts/{AccountSid}/Applications.json |  |
| [**deleteApplication**](Api20100401ApplicationApi.md#deleteApplication) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json |  |
| [**fetchApplication**](Api20100401ApplicationApi.md#fetchApplication) | **GET** /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json |  |
| [**listApplication**](Api20100401ApplicationApi.md#listApplication) | **GET** /2010-04-01/Accounts/{AccountSid}/Applications.json |  |
| [**updateApplication**](Api20100401ApplicationApi.md#updateApplication) | **POST** /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json |  |


<a id="createApplication"></a>
# **createApplication**
> ApiV2010AccountApplication createApplication(accountSid, apiVersion, friendlyName, messageStatusCallback, publicApplicationConnectEnabled, smsFallbackMethod, smsFallbackUrl, smsMethod, smsStatusCallback, smsUrl, statusCallback, statusCallbackMethod, voiceCallerIdLookup, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl)



Create a new application within your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ApplicationApi apiInstance = new Api20100401ApplicationApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. The default value is the account's default API version.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new application. It can be up to 64 characters long.
    URI messageStatusCallback = new URI(); // URI | The URL we should call using a POST method to send message status information to your application.
    Boolean publicApplicationConnectEnabled = true; // Boolean | Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: `true` or `false`.
    String smsFallbackMethod = "HEAD"; // String | The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`.
    URI smsFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs while retrieving or executing the TwiML from `sms_url`.
    String smsMethod = "HEAD"; // String | The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`.
    URI smsStatusCallback = new URI(); // URI | The URL we should call using a POST method to send status information about SMS messages sent by the application.
    URI smsUrl = new URI(); // URI | The URL we should call when the phone number receives an incoming SMS message.
    URI statusCallback = new URI(); // URI | The URL we should call using the `status_callback_method` to send status information to your application.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`.
    Boolean voiceCallerIdLookup = true; // Boolean | Whether we should look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`.
    String voiceFallbackMethod = "HEAD"; // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
    URI voiceFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
    String voiceMethod = "HEAD"; // String | The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
    URI voiceUrl = new URI(); // URI | The URL we should call when the phone number assigned to this application receives a call.
    try {
      ApiV2010AccountApplication result = apiInstance.createApplication(accountSid, apiVersion, friendlyName, messageStatusCallback, publicApplicationConnectEnabled, smsFallbackMethod, smsFallbackUrl, smsMethod, smsStatusCallback, smsUrl, statusCallback, statusCallbackMethod, voiceCallerIdLookup, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ApplicationApi#createApplication");
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
| **apiVersion** | **String**| The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;. The default value is the account&#39;s default API version. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the new application. It can be up to 64 characters long. | [optional] |
| **messageStatusCallback** | **URI**| The URL we should call using a POST method to send message status information to your application. | [optional] |
| **publicApplicationConnectEnabled** | **Boolean**| Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **smsFallbackMethod** | **String**| The HTTP method we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsFallbackUrl** | **URI**| The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. | [optional] |
| **smsMethod** | **String**| The HTTP method we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsStatusCallback** | **URI**| The URL we should call using a POST method to send status information about SMS messages sent by the application. | [optional] |
| **smsUrl** | **URI**| The URL we should call when the phone number receives an incoming SMS message. | [optional] |
| **statusCallback** | **URI**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceCallerIdLookup** | **Boolean**| Whether we should look up the caller&#39;s caller-ID name from the CNAM database (additional charges apply). Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceFallbackUrl** | **URI**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional] |
| **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceUrl** | **URI**| The URL we should call when the phone number assigned to this application receives a call. | [optional] |

### Return type

[**ApiV2010AccountApplication**](ApiV2010AccountApplication.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteApplication"></a>
# **deleteApplication**
> deleteApplication(accountSid, sid)



Delete the application by the specified application sid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ApplicationApi apiInstance = new Api20100401ApplicationApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Application resource to delete.
    try {
      apiInstance.deleteApplication(accountSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ApplicationApi#deleteApplication");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Application resource to delete. | |

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

<a id="fetchApplication"></a>
# **fetchApplication**
> ApiV2010AccountApplication fetchApplication(accountSid, sid)



Fetch the application specified by the provided sid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ApplicationApi apiInstance = new Api20100401ApplicationApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Application resource to fetch.
    try {
      ApiV2010AccountApplication result = apiInstance.fetchApplication(accountSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ApplicationApi#fetchApplication");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Application resource to fetch. | |

### Return type

[**ApiV2010AccountApplication**](ApiV2010AccountApplication.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listApplication"></a>
# **listApplication**
> ListApplicationResponse listApplication(accountSid, friendlyName, pageSize, page, pageToken)



Retrieve a list of applications representing an application within the requesting account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ApplicationApi apiInstance = new Api20100401ApplicationApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to read.
    String friendlyName = "friendlyName_example"; // String | The string that identifies the Application resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListApplicationResponse result = apiInstance.listApplication(accountSid, friendlyName, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ApplicationApi#listApplication");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to read. | |
| **friendlyName** | **String**| The string that identifies the Application resources to read. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListApplicationResponse**](ListApplicationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateApplication"></a>
# **updateApplication**
> ApiV2010AccountApplication updateApplication(accountSid, sid, apiVersion, friendlyName, messageStatusCallback, publicApplicationConnectEnabled, smsFallbackMethod, smsFallbackUrl, smsMethod, smsStatusCallback, smsUrl, statusCallback, statusCallbackMethod, voiceCallerIdLookup, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl)



Updates the application&#39;s properties

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ApplicationApi apiInstance = new Api20100401ApplicationApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Application resource to update.
    String apiVersion = "apiVersion_example"; // String | The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. The default value is your account's default API version.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    URI messageStatusCallback = new URI(); // URI | The URL we should call using a POST method to send message status information to your application.
    Boolean publicApplicationConnectEnabled = true; // Boolean | Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: `true` or `false`.
    String smsFallbackMethod = "HEAD"; // String | The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`.
    URI smsFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs while retrieving or executing the TwiML from `sms_url`.
    String smsMethod = "HEAD"; // String | The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`.
    URI smsStatusCallback = new URI(); // URI | Same as message_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application. Deprecated, included for backwards compatibility.
    URI smsUrl = new URI(); // URI | The URL we should call when the phone number receives an incoming SMS message.
    URI statusCallback = new URI(); // URI | The URL we should call using the `status_callback_method` to send status information to your application.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`.
    Boolean voiceCallerIdLookup = true; // Boolean | Whether we should look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`.
    String voiceFallbackMethod = "HEAD"; // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
    URI voiceFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
    String voiceMethod = "HEAD"; // String | The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
    URI voiceUrl = new URI(); // URI | The URL we should call when the phone number assigned to this application receives a call.
    try {
      ApiV2010AccountApplication result = apiInstance.updateApplication(accountSid, sid, apiVersion, friendlyName, messageStatusCallback, publicApplicationConnectEnabled, smsFallbackMethod, smsFallbackUrl, smsMethod, smsStatusCallback, smsUrl, statusCallback, statusCallbackMethod, voiceCallerIdLookup, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ApplicationApi#updateApplication");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Application resource to update. | |
| **apiVersion** | **String**| The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;. The default value is your account&#39;s default API version. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **messageStatusCallback** | **URI**| The URL we should call using a POST method to send message status information to your application. | [optional] |
| **publicApplicationConnectEnabled** | **Boolean**| Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **smsFallbackMethod** | **String**| The HTTP method we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsFallbackUrl** | **URI**| The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. | [optional] |
| **smsMethod** | **String**| The HTTP method we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsStatusCallback** | **URI**| Same as message_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application. Deprecated, included for backwards compatibility. | [optional] |
| **smsUrl** | **URI**| The URL we should call when the phone number receives an incoming SMS message. | [optional] |
| **statusCallback** | **URI**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceCallerIdLookup** | **Boolean**| Whether we should look up the caller&#39;s caller-ID name from the CNAM database (additional charges apply). Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceFallbackUrl** | **URI**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional] |
| **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceUrl** | **URI**| The URL we should call when the phone number assigned to this application receives a call. | [optional] |

### Return type

[**ApiV2010AccountApplication**](ApiV2010AccountApplication.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

