# VoiceV1ByocTrunkApi

All URIs are relative to *https://voice.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createByocTrunk**](VoiceV1ByocTrunkApi.md#createByocTrunk) | **POST** /v1/ByocTrunks |  |
| [**deleteByocTrunk**](VoiceV1ByocTrunkApi.md#deleteByocTrunk) | **DELETE** /v1/ByocTrunks/{Sid} |  |
| [**fetchByocTrunk**](VoiceV1ByocTrunkApi.md#fetchByocTrunk) | **GET** /v1/ByocTrunks/{Sid} |  |
| [**listByocTrunk**](VoiceV1ByocTrunkApi.md#listByocTrunk) | **GET** /v1/ByocTrunks |  |
| [**updateByocTrunk**](VoiceV1ByocTrunkApi.md#updateByocTrunk) | **POST** /v1/ByocTrunks/{Sid} |  |


<a id="createByocTrunk"></a>
# **createByocTrunk**
> VoiceV1ByocTrunk createByocTrunk(cnamLookupEnabled, connectionPolicySid, friendlyName, fromDomainSid, statusCallbackMethod, statusCallbackUrl, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1ByocTrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1ByocTrunkApi apiInstance = new VoiceV1ByocTrunkApi(defaultClient);
    Boolean cnamLookupEnabled = true; // Boolean | Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    String connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    String fromDomainSid = "fromDomainSid_example"; // String | The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\"call back\\\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\"sip.twilio.com\\\".
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
    URI statusCallbackUrl = new URI(); // URI | The URL that we should call to pass status parameters (such as call ended) to your application.
    String voiceFallbackMethod = "HEAD"; // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
    URI voiceFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs while retrieving or executing the TwiML from `voice_url`.
    String voiceMethod = "HEAD"; // String | The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
    URI voiceUrl = new URI(); // URI | The URL we should call when the BYOC Trunk receives a call.
    try {
      VoiceV1ByocTrunk result = apiInstance.createByocTrunk(cnamLookupEnabled, connectionPolicySid, friendlyName, fromDomainSid, statusCallbackMethod, statusCallbackUrl, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1ByocTrunkApi#createByocTrunk");
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
| **cnamLookupEnabled** | **Boolean**| Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information. | [optional] |
| **connectionPolicySid** | **String**| The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] |
| **fromDomainSid** | **String**| The SID of the SIP Domain that should be used in the &#x60;From&#x60; header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\&quot;call back\\\&quot; an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\&quot;sip.twilio.com\\\&quot;. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **statusCallbackUrl** | **URI**| The URL that we should call to pass status parameters (such as call ended) to your application. | [optional] |
| **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceFallbackUrl** | **URI**| The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;voice_url&#x60;. | [optional] |
| **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceUrl** | **URI**| The URL we should call when the BYOC Trunk receives a call. | [optional] |

### Return type

[**VoiceV1ByocTrunk**](VoiceV1ByocTrunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteByocTrunk"></a>
# **deleteByocTrunk**
> deleteByocTrunk(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1ByocTrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1ByocTrunkApi apiInstance = new VoiceV1ByocTrunkApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the BYOC Trunk resource to delete.
    try {
      apiInstance.deleteByocTrunk(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1ByocTrunkApi#deleteByocTrunk");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the BYOC Trunk resource to delete. | |

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

<a id="fetchByocTrunk"></a>
# **fetchByocTrunk**
> VoiceV1ByocTrunk fetchByocTrunk(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1ByocTrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1ByocTrunkApi apiInstance = new VoiceV1ByocTrunkApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch.
    try {
      VoiceV1ByocTrunk result = apiInstance.fetchByocTrunk(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1ByocTrunkApi#fetchByocTrunk");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch. | |

### Return type

[**VoiceV1ByocTrunk**](VoiceV1ByocTrunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listByocTrunk"></a>
# **listByocTrunk**
> ListByocTrunkResponse listByocTrunk(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1ByocTrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1ByocTrunkApi apiInstance = new VoiceV1ByocTrunkApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListByocTrunkResponse result = apiInstance.listByocTrunk(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1ByocTrunkApi#listByocTrunk");
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

[**ListByocTrunkResponse**](ListByocTrunkResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateByocTrunk"></a>
# **updateByocTrunk**
> VoiceV1ByocTrunk updateByocTrunk(sid, cnamLookupEnabled, connectionPolicySid, friendlyName, fromDomainSid, statusCallbackMethod, statusCallbackUrl, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1ByocTrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1ByocTrunkApi apiInstance = new VoiceV1ByocTrunkApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update.
    Boolean cnamLookupEnabled = true; // Boolean | Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    String connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    String fromDomainSid = "fromDomainSid_example"; // String | The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\"call back\\\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\"sip.twilio.com\\\".
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
    URI statusCallbackUrl = new URI(); // URI | The URL that we should call to pass status parameters (such as call ended) to your application.
    String voiceFallbackMethod = "HEAD"; // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
    URI voiceFallbackUrl = new URI(); // URI | The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.
    String voiceMethod = "HEAD"; // String | The HTTP method we should use to call `voice_url`
    URI voiceUrl = new URI(); // URI | The URL we should call when the BYOC Trunk receives a call.
    try {
      VoiceV1ByocTrunk result = apiInstance.updateByocTrunk(sid, cnamLookupEnabled, connectionPolicySid, friendlyName, fromDomainSid, statusCallbackMethod, statusCallbackUrl, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1ByocTrunkApi#updateByocTrunk");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update. | |
| **cnamLookupEnabled** | **Boolean**| Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information. | [optional] |
| **connectionPolicySid** | **String**| The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] |
| **fromDomainSid** | **String**| The SID of the SIP Domain that should be used in the &#x60;From&#x60; header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\&quot;call back\\\&quot; an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\&quot;sip.twilio.com\\\&quot;. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **statusCallbackUrl** | **URI**| The URL that we should call to pass status parameters (such as call ended) to your application. | [optional] |
| **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceFallbackUrl** | **URI**| The URL that we should call when an error occurs while retrieving or executing the TwiML requested by &#x60;voice_url&#x60;. | [optional] |
| **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60; | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceUrl** | **URI**| The URL we should call when the BYOC Trunk receives a call. | [optional] |

### Return type

[**VoiceV1ByocTrunk**](VoiceV1ByocTrunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

