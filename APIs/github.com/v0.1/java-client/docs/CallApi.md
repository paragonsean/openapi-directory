# CallApi

All URIs are relative to *https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v01BulkCallPost**](CallApi.md#v01BulkCallPost) | **POST** /v0.1/BulkCall/ | /v0.1/BulkCall/ |
| [**v01CallPost**](CallApi.md#v01CallPost) | **POST** /v0.1/Call/ | /v0.1/Call/ |
| [**v01CancelScheduledHangupPost**](CallApi.md#v01CancelScheduledHangupPost) | **POST** /v0.1/CancelScheduledHangup/ | /v0.1/CancelScheduledHangup/ |
| [**v01CancelScheduledPlayPost**](CallApi.md#v01CancelScheduledPlayPost) | **POST** /v0.1/CancelScheduledPlay/ | /v0.1/CancelScheduledPlay/ |
| [**v01GroupCallPost**](CallApi.md#v01GroupCallPost) | **POST** /v0.1/GroupCall/ | /v0.1/GroupCall/ |
| [**v01HangupAllCallsPost**](CallApi.md#v01HangupAllCallsPost) | **POST** /v0.1/HangupAllCalls/ | /v0.1/HangupAllCalls/ |
| [**v01HangupCallPost**](CallApi.md#v01HangupCallPost) | **POST** /v0.1/HangupCall/ | /v0.1/HangupCall/ |
| [**v01PlayPost**](CallApi.md#v01PlayPost) | **POST** /v0.1/Play/ | /v0.1/Play/ |
| [**v01PlayStopPost**](CallApi.md#v01PlayStopPost) | **POST** /v0.1/PlayStop/ | /v0.1/PlayStop/ |
| [**v01RecordStartPost**](CallApi.md#v01RecordStartPost) | **POST** /v0.1/RecordStart/ | /v0.1/RecordStart/ |
| [**v01RecordStopPost**](CallApi.md#v01RecordStopPost) | **POST** /v0.1/RecordStop/ | /v0.1/RecordStop/ |
| [**v01ScheduleHangupPost**](CallApi.md#v01ScheduleHangupPost) | **POST** /v0.1/ScheduleHangup/ | /v0.1/ScheduleHangup/ |
| [**v01SchedulePlayPost**](CallApi.md#v01SchedulePlayPost) | **POST** /v0.1/SchedulePlay/ | /v0.1/SchedulePlay/ |
| [**v01SendDigitsPost**](CallApi.md#v01SendDigitsPost) | **POST** /v0.1/SendDigits/ | /v0.1/SendDigits/ |
| [**v01SoundTouchPost**](CallApi.md#v01SoundTouchPost) | **POST** /v0.1/SoundTouch/ | /v0.1/SoundTouch/ |
| [**v01SoundTouchStopPost**](CallApi.md#v01SoundTouchStopPost) | **POST** /v0.1/SoundTouchStop/ | /v0.1/SoundTouchStop/ |
| [**v01TransferCallPost**](CallApi.md#v01TransferCallPost) | **POST** /v0.1/TransferCall/ | /v0.1/TransferCall/ |


<a id="v01BulkCallPost"></a>
# **v01BulkCallPost**
> BulkCallResponse v01BulkCallPost(answerUrl, delimiter, from, gateways, to, callerName, confirmKey, confirmSound, coreUUID, extraDialString, gatewayCodecs, gatewayRetries, gatewayTimeouts, hangupOnRing, hangupUrl, rejectCauses, ringUrl, sendDigits, sendOnPreanswer, timeLimit)

/v0.1/BulkCall/

Initiates multiple concurrent outbound calls

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String answerUrl = "answerUrl_example"; // String | Fully qualified URL which will provide the RestXML once the call connects
    String delimiter = "delimiter_example"; // String | Any character, except `/` and `,`, which will be used as a separator within several parameters
    String from = "from_example"; // String | Phone number to be used as Caller ID
    String gateways = "gateways_example"; // String | Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)
    String to = "to_example"; // String | Phone number to be called
    String callerName = "callerName_example"; // String | Caller Name to be set for the call
    String confirmKey = "confirmKey_example"; // String | DTMF tone the called party must send to accept the call
    String confirmSound = "confirmSound_example"; // String | Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered
    String coreUUID = "coreUUID_example"; // String | Core UUID of the desired FreeSWITCH instance (an Eqivo extension)
    String extraDialString = "extraDialString_example"; // String | Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.
    String gatewayCodecs = "gatewayCodecs_example"; // String | List of codec(s) to be used for each gateway. Enclose codec groups in single quotes
    String gatewayRetries = "gatewayRetries_example"; // String | List of maximum retry counts for each gateway
    String gatewayTimeouts = "gatewayTimeouts_example"; // String | List of maximum timeout amounts (in seconds) for each gateway
    Integer hangupOnRing = 56; // Integer | Schedules the call's hangup at a given time offset (in seconds) after the destination starts ringing
    String hangupUrl = "hangupUrl_example"; // String | Fully qualified URL to which the call hangup notification will be POSTed. `HangupCause` is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)
    String rejectCauses = "NO_ANSWER,ORIGINATOR_CANCEL,ALLOTTED_TIMEOUT,NO_USER_RESPONSE,CALL_REJECTED"; // String | Comma separated reject causes
    String ringUrl = "ringUrl_example"; // String | Fully qualified URL to which the call ringing notification will be POSTed. `RequestUUID` and `CallUUID` is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)
    String sendDigits = "sendDigits_example"; // String | DTMF tones to be sent when the call is answered. Each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string
    Boolean sendOnPreanswer = true; // Boolean | When set to `true`, DTMF tones will be sent as early media rather than when the call is answered
    Integer timeLimit = 56; // Integer | Schedules the call's hangup at a given time offset (in seconds) after the call is answered
    try {
      BulkCallResponse result = apiInstance.v01BulkCallPost(answerUrl, delimiter, from, gateways, to, callerName, confirmKey, confirmSound, coreUUID, extraDialString, gatewayCodecs, gatewayRetries, gatewayTimeouts, hangupOnRing, hangupUrl, rejectCauses, ringUrl, sendDigits, sendOnPreanswer, timeLimit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01BulkCallPost");
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
| **answerUrl** | **String**| Fully qualified URL which will provide the RestXML once the call connects | |
| **delimiter** | **String**| Any character, except &#x60;/&#x60; and &#x60;,&#x60;, which will be used as a separator within several parameters | |
| **from** | **String**| Phone number to be used as Caller ID | |
| **gateways** | **String**| Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover) | |
| **to** | **String**| Phone number to be called | |
| **callerName** | **String**| Caller Name to be set for the call | [optional] |
| **confirmKey** | **String**| DTMF tone the called party must send to accept the call | [optional] |
| **confirmSound** | **String**| Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered | [optional] |
| **coreUUID** | **String**| Core UUID of the desired FreeSWITCH instance (an Eqivo extension) | [optional] |
| **extraDialString** | **String**| Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call. | [optional] |
| **gatewayCodecs** | **String**| List of codec(s) to be used for each gateway. Enclose codec groups in single quotes | [optional] |
| **gatewayRetries** | **String**| List of maximum retry counts for each gateway | [optional] |
| **gatewayTimeouts** | **String**| List of maximum timeout amounts (in seconds) for each gateway | [optional] |
| **hangupOnRing** | **Integer**| Schedules the call&#39;s hangup at a given time offset (in seconds) after the destination starts ringing | [optional] |
| **hangupUrl** | **String**| Fully qualified URL to which the call hangup notification will be POSTed. &#x60;HangupCause&#x60; is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters) | [optional] |
| **rejectCauses** | **String**| Comma separated reject causes | [optional] [default to NO_ANSWER,ORIGINATOR_CANCEL,ALLOTTED_TIMEOUT,NO_USER_RESPONSE,CALL_REJECTED] |
| **ringUrl** | **String**| Fully qualified URL to which the call ringing notification will be POSTed. &#x60;RequestUUID&#x60; and &#x60;CallUUID&#x60; is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters) | [optional] |
| **sendDigits** | **String**| DTMF tones to be sent when the call is answered. Each occurrence of &#x60;w&#x60; implies a 0.5 seconds delay whereas &#x60;W&#x60; will apply a whole second delay. To alter the tone duration (by default, 2000ms), append &#x60;@&#x60; and the length in milliseconds at the end of the string | [optional] |
| **sendOnPreanswer** | **Boolean**| When set to &#x60;true&#x60;, DTMF tones will be sent as early media rather than when the call is answered | [optional] |
| **timeLimit** | **Integer**| Schedules the call&#39;s hangup at a given time offset (in seconds) after the call is answered | [optional] |

### Return type

[**BulkCallResponse**](BulkCallResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01CallPost"></a>
# **v01CallPost**
> CallResponse v01CallPost(answerUrl, from, gateways, to, asyncAMD, asyncAmdStatusCallback, asyncAmdStatusCallbackMethod, callerName, coreUUID, extraDialString, gatewayCodecs, gatewayRetries, gatewayTimeouts, hangupOnRing, hangupUrl, machineDetection, machineDetectionSilenceTimeout, machineDetectionSpeechEndThreshold, machineDetectionSpeechThreshold, machineDetectionTimeout, ringUrl, sendDigits, sendOnPreanswer, timeLimit)

/v0.1/Call/

Initiates an outbound call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String answerUrl = "answerUrl_example"; // String | Fully qualified URL which will provide the RestXML once the call connects
    String from = "from_example"; // String | Phone number to be used as Caller ID
    String gateways = "gateways_example"; // String | Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)
    String to = "to_example"; // String | Phone number to be called
    Boolean asyncAMD = false; // Boolean | When set to `true`, the call flow execution is blocked until answering machine detection is complete (an Eqivo extension)
    String asyncAmdStatusCallback = "asyncAmdStatusCallback_example"; // String | Fully qualified URL to which the answering machine detection result will be sent. `AnsweredBy` and `MachineDetectionDuration` are appended to the usual [call notification parameters](#/components/schemas/CallNotificationParameters) (an Eqivo extension)
    String asyncAmdStatusCallbackMethod = "POST"; // String | HTTP method to be used when answering machine detection is completed (an Eqivo extension)
    String callerName = "callerName_example"; // String | Caller Name to be set for the call
    String coreUUID = "coreUUID_example"; // String | Core UUID of the desired FreeSWITCH instance (an Eqivo extension)
    String extraDialString = "extraDialString_example"; // String | Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.
    String gatewayCodecs = "gatewayCodecs_example"; // String | List of codec(s) to be used for each gateway. Enclose codec groups in single quotes
    String gatewayRetries = "gatewayRetries_example"; // String | List of maximum retry counts for each gateway
    String gatewayTimeouts = "gatewayTimeouts_example"; // String | List of maximum timeout amounts (in seconds) for each gateway
    Integer hangupOnRing = 56; // Integer | Schedules the call's hangup at a given time offset (in seconds) after the destination starts ringing
    String hangupUrl = "hangupUrl_example"; // String | Fully qualified URL to which the call hangup notification will be POSTed. `HangupCause` is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)
    String machineDetection = "Enable"; // String | Enables answering machine detection; optionally, it waits until the greeting message has been played back (an Eqivo extension)
    Integer machineDetectionSilenceTimeout = 5000; // Integer | Initial silence threshold (in milliseconds, an Eqivo extension)
    Integer machineDetectionSpeechEndThreshold = 1200; // Integer | Silence threshold (in milliseconds, an Eqivo extension)
    Integer machineDetectionSpeechThreshold = 2400; // Integer | Speech activity/utterance threshold (in milliseconds, an Eqivo extension)
    Integer machineDetectionTimeout = 30; // Integer | Amount of time (in seconds) allotted for answering machine detection assessment (an Eqivo extension)
    String ringUrl = "ringUrl_example"; // String | Fully qualified URL to which the call ringing notification will be POSTed. `RequestUUID` and `CallUUID` is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)
    String sendDigits = "sendDigits_example"; // String | DTMF tones to be sent when the call is answered. Each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string
    Boolean sendOnPreanswer = true; // Boolean | When set to `true`, DTMF tones will be sent as early media rather than when the call is answered
    Integer timeLimit = 56; // Integer | Schedules the call's hangup at a given time offset (in seconds) after the call is answered
    try {
      CallResponse result = apiInstance.v01CallPost(answerUrl, from, gateways, to, asyncAMD, asyncAmdStatusCallback, asyncAmdStatusCallbackMethod, callerName, coreUUID, extraDialString, gatewayCodecs, gatewayRetries, gatewayTimeouts, hangupOnRing, hangupUrl, machineDetection, machineDetectionSilenceTimeout, machineDetectionSpeechEndThreshold, machineDetectionSpeechThreshold, machineDetectionTimeout, ringUrl, sendDigits, sendOnPreanswer, timeLimit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01CallPost");
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
| **answerUrl** | **String**| Fully qualified URL which will provide the RestXML once the call connects | |
| **from** | **String**| Phone number to be used as Caller ID | |
| **gateways** | **String**| Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover) | |
| **to** | **String**| Phone number to be called | |
| **asyncAMD** | **Boolean**| When set to &#x60;true&#x60;, the call flow execution is blocked until answering machine detection is complete (an Eqivo extension) | [optional] [default to false] |
| **asyncAmdStatusCallback** | **String**| Fully qualified URL to which the answering machine detection result will be sent. &#x60;AnsweredBy&#x60; and &#x60;MachineDetectionDuration&#x60; are appended to the usual [call notification parameters](#/components/schemas/CallNotificationParameters) (an Eqivo extension) | [optional] |
| **asyncAmdStatusCallbackMethod** | **String**| HTTP method to be used when answering machine detection is completed (an Eqivo extension) | [optional] [default to POST] [enum: POST, GET] |
| **callerName** | **String**| Caller Name to be set for the call | [optional] |
| **coreUUID** | **String**| Core UUID of the desired FreeSWITCH instance (an Eqivo extension) | [optional] |
| **extraDialString** | **String**| Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call. | [optional] |
| **gatewayCodecs** | **String**| List of codec(s) to be used for each gateway. Enclose codec groups in single quotes | [optional] |
| **gatewayRetries** | **String**| List of maximum retry counts for each gateway | [optional] |
| **gatewayTimeouts** | **String**| List of maximum timeout amounts (in seconds) for each gateway | [optional] |
| **hangupOnRing** | **Integer**| Schedules the call&#39;s hangup at a given time offset (in seconds) after the destination starts ringing | [optional] |
| **hangupUrl** | **String**| Fully qualified URL to which the call hangup notification will be POSTed. &#x60;HangupCause&#x60; is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters) | [optional] |
| **machineDetection** | **String**| Enables answering machine detection; optionally, it waits until the greeting message has been played back (an Eqivo extension) | [optional] [enum: Enable, DetectMessageEnd] |
| **machineDetectionSilenceTimeout** | **Integer**| Initial silence threshold (in milliseconds, an Eqivo extension) | [optional] [default to 5000] |
| **machineDetectionSpeechEndThreshold** | **Integer**| Silence threshold (in milliseconds, an Eqivo extension) | [optional] [default to 1200] |
| **machineDetectionSpeechThreshold** | **Integer**| Speech activity/utterance threshold (in milliseconds, an Eqivo extension) | [optional] [default to 2400] |
| **machineDetectionTimeout** | **Integer**| Amount of time (in seconds) allotted for answering machine detection assessment (an Eqivo extension) | [optional] [default to 30] |
| **ringUrl** | **String**| Fully qualified URL to which the call ringing notification will be POSTed. &#x60;RequestUUID&#x60; and &#x60;CallUUID&#x60; is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters) | [optional] |
| **sendDigits** | **String**| DTMF tones to be sent when the call is answered. Each occurrence of &#x60;w&#x60; implies a 0.5 seconds delay whereas &#x60;W&#x60; will apply a whole second delay. To alter the tone duration (by default, 2000ms), append &#x60;@&#x60; and the length in milliseconds at the end of the string | [optional] |
| **sendOnPreanswer** | **Boolean**| When set to &#x60;true&#x60;, DTMF tones will be sent as early media rather than when the call is answered | [optional] |
| **timeLimit** | **Integer**| Schedules the call&#39;s hangup at a given time offset (in seconds) after the call is answered | [optional] |

### Return type

[**CallResponse**](CallResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01CancelScheduledHangupPost"></a>
# **v01CancelScheduledHangupPost**
> CancelScheduledHangupResponse v01CancelScheduledHangupPost(schedHangupId)

/v0.1/CancelScheduledHangup/

Cancels a scheduled hangup for a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String schedHangupId = "schedHangupId_example"; // String | Unique identifier returned when scheduled hangup was originally requested
    try {
      CancelScheduledHangupResponse result = apiInstance.v01CancelScheduledHangupPost(schedHangupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01CancelScheduledHangupPost");
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
| **schedHangupId** | **String**| Unique identifier returned when scheduled hangup was originally requested | |

### Return type

[**CancelScheduledHangupResponse**](CancelScheduledHangupResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01CancelScheduledPlayPost"></a>
# **v01CancelScheduledPlayPost**
> CancelScheduledPlayResponse v01CancelScheduledPlayPost(schedPlayId)

/v0.1/CancelScheduledPlay/

Cancels a scheduled playback request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String schedPlayId = "schedPlayId_example"; // String | Unique identifier returned when scheduled playback was originally requested
    try {
      CancelScheduledPlayResponse result = apiInstance.v01CancelScheduledPlayPost(schedPlayId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01CancelScheduledPlayPost");
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
| **schedPlayId** | **String**| Unique identifier returned when scheduled playback was originally requested | |

### Return type

[**CancelScheduledPlayResponse**](CancelScheduledPlayResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01GroupCallPost"></a>
# **v01GroupCallPost**
> GroupCallResponse v01GroupCallPost(answerUrl, delimiter, from, gateways, to, callerName, confirmKey, confirmSound, coreUUID, extraDialString, gatewayCodecs, gatewayRetries, gatewayTimeouts, hangupOnRing, hangupUrl, rejectCauses, ringUrl, sendDigits, sendOnPreanswer, timeLimit)

/v0.1/GroupCall/

Initiate multiple racing outbound calls

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String answerUrl = "answerUrl_example"; // String | Fully qualified URL which will provide the RestXML once the call connects
    String delimiter = "delimiter_example"; // String | Any character, except `/` and `,`, which will be used as a separator within several parameters
    String from = "from_example"; // String | Phone number to be used as Caller ID
    String gateways = "gateways_example"; // String | Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)
    String to = "to_example"; // String | Phone number to be called
    String callerName = "callerName_example"; // String | Caller Name to be set for the call
    String confirmKey = "confirmKey_example"; // String | DTMF tone the called party must send to accept the call
    String confirmSound = "confirmSound_example"; // String | Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered
    String coreUUID = "coreUUID_example"; // String | Core UUID of the desired FreeSWITCH instance (an Eqivo extension)
    String extraDialString = "extraDialString_example"; // String | Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.
    String gatewayCodecs = "gatewayCodecs_example"; // String | List of codec(s) to be used for each gateway. Enclose codec groups in single quotes
    String gatewayRetries = "gatewayRetries_example"; // String | List of maximum retry counts for each gateway
    String gatewayTimeouts = "gatewayTimeouts_example"; // String | List of maximum timeout amounts (in seconds) for each gateway
    Integer hangupOnRing = 56; // Integer | Schedules the call's hangup at a given time offset (in seconds) after the destination starts ringing
    String hangupUrl = "hangupUrl_example"; // String | Fully qualified URL to which the call hangup notification will be POSTed. `HangupCause` is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)
    String rejectCauses = "NO_ANSWER,ORIGINATOR_CANCEL,ALLOTTED_TIMEOUT,NO_USER_RESPONSE,CALL_REJECTED"; // String | Comma separated reject causes
    String ringUrl = "ringUrl_example"; // String | Fully qualified URL to which the call ringing notification will be POSTed. `RequestUUID` and `CallUUID` is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)
    String sendDigits = "sendDigits_example"; // String | DTMF tones to be sent when the call is answered. Each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string
    Boolean sendOnPreanswer = true; // Boolean | When set to `true`, DTMF tones will be sent as early media rather than when the call is answered
    Integer timeLimit = 56; // Integer | Schedules the call's hangup at a given time offset (in seconds) after the call is answered
    try {
      GroupCallResponse result = apiInstance.v01GroupCallPost(answerUrl, delimiter, from, gateways, to, callerName, confirmKey, confirmSound, coreUUID, extraDialString, gatewayCodecs, gatewayRetries, gatewayTimeouts, hangupOnRing, hangupUrl, rejectCauses, ringUrl, sendDigits, sendOnPreanswer, timeLimit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01GroupCallPost");
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
| **answerUrl** | **String**| Fully qualified URL which will provide the RestXML once the call connects | |
| **delimiter** | **String**| Any character, except &#x60;/&#x60; and &#x60;,&#x60;, which will be used as a separator within several parameters | |
| **from** | **String**| Phone number to be used as Caller ID | |
| **gateways** | **String**| Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover) | |
| **to** | **String**| Phone number to be called | |
| **callerName** | **String**| Caller Name to be set for the call | [optional] |
| **confirmKey** | **String**| DTMF tone the called party must send to accept the call | [optional] |
| **confirmSound** | **String**| Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered | [optional] |
| **coreUUID** | **String**| Core UUID of the desired FreeSWITCH instance (an Eqivo extension) | [optional] |
| **extraDialString** | **String**| Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call. | [optional] |
| **gatewayCodecs** | **String**| List of codec(s) to be used for each gateway. Enclose codec groups in single quotes | [optional] |
| **gatewayRetries** | **String**| List of maximum retry counts for each gateway | [optional] |
| **gatewayTimeouts** | **String**| List of maximum timeout amounts (in seconds) for each gateway | [optional] |
| **hangupOnRing** | **Integer**| Schedules the call&#39;s hangup at a given time offset (in seconds) after the destination starts ringing | [optional] |
| **hangupUrl** | **String**| Fully qualified URL to which the call hangup notification will be POSTed. &#x60;HangupCause&#x60; is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters) | [optional] |
| **rejectCauses** | **String**| Comma separated reject causes | [optional] [default to NO_ANSWER,ORIGINATOR_CANCEL,ALLOTTED_TIMEOUT,NO_USER_RESPONSE,CALL_REJECTED] |
| **ringUrl** | **String**| Fully qualified URL to which the call ringing notification will be POSTed. &#x60;RequestUUID&#x60; and &#x60;CallUUID&#x60; is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters) | [optional] |
| **sendDigits** | **String**| DTMF tones to be sent when the call is answered. Each occurrence of &#x60;w&#x60; implies a 0.5 seconds delay whereas &#x60;W&#x60; will apply a whole second delay. To alter the tone duration (by default, 2000ms), append &#x60;@&#x60; and the length in milliseconds at the end of the string | [optional] |
| **sendOnPreanswer** | **Boolean**| When set to &#x60;true&#x60;, DTMF tones will be sent as early media rather than when the call is answered | [optional] |
| **timeLimit** | **Integer**| Schedules the call&#39;s hangup at a given time offset (in seconds) after the call is answered | [optional] |

### Return type

[**GroupCallResponse**](GroupCallResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01HangupAllCallsPost"></a>
# **v01HangupAllCallsPost**
> HangupAllCallsResponse v01HangupAllCallsPost()

/v0.1/HangupAllCalls/

Hangs up all established calls

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    try {
      HangupAllCallsResponse result = apiInstance.v01HangupAllCallsPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01HangupAllCallsPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HangupAllCallsResponse**](HangupAllCallsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01HangupCallPost"></a>
# **v01HangupCallPost**
> HangupCallResponse v01HangupCallPost(callUUID, requestUUID)

/v0.1/HangupCall/

Hangs up a specific call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String callUUID = "callUUID_example"; // String | Unique identifier of the call (when established); this parameter is mutually exclusive with RequestUUID
    String requestUUID = "requestUUID_example"; // String | Unique identifier of the API request (when the call is not established yet); this parameter is mutually exclusive with CallUUID
    try {
      HangupCallResponse result = apiInstance.v01HangupCallPost(callUUID, requestUUID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01HangupCallPost");
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
| **callUUID** | **String**| Unique identifier of the call (when established); this parameter is mutually exclusive with RequestUUID | [optional] |
| **requestUUID** | **String**| Unique identifier of the API request (when the call is not established yet); this parameter is mutually exclusive with CallUUID | [optional] |

### Return type

[**HangupCallResponse**](HangupCallResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01PlayPost"></a>
# **v01PlayPost**
> PlayResponse v01PlayPost(callUUID, sounds, legs, length, loop, mix)

/v0.1/Play/

Plays media into a live call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String callUUID = "callUUID_example"; // String | Unique identifier of the call to play media into
    String sounds = "sounds_example"; // String | Comma separated list of file paths/URIs to be played
    String legs = "aleg"; // String | Call leg(s) for which the media will be played; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.
    Integer length = 3600; // Integer | Maximum amount of time (in seconds) to playback the media
    Boolean loop = false; // Boolean | Loops the media file(s) indefinitely
    Boolean mix = true; // Boolean | Whether the media should be mixed with the call's audio stream
    try {
      PlayResponse result = apiInstance.v01PlayPost(callUUID, sounds, legs, length, loop, mix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01PlayPost");
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
| **callUUID** | **String**| Unique identifier of the call to play media into | |
| **sounds** | **String**| Comma separated list of file paths/URIs to be played | |
| **legs** | **String**| Call leg(s) for which the media will be played; &#x60;aleg&#x60; refers to the initial call leg, &#x60;bleg&#x60; refers to the bridged call leg, if applicable. | [optional] [default to aleg] [enum: aleg, bleg, both] |
| **length** | **Integer**| Maximum amount of time (in seconds) to playback the media | [optional] [default to 3600] |
| **loop** | **Boolean**| Loops the media file(s) indefinitely | [optional] [default to false] |
| **mix** | **Boolean**| Whether the media should be mixed with the call&#39;s audio stream | [optional] [default to true] |

### Return type

[**PlayResponse**](PlayResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01PlayStopPost"></a>
# **v01PlayStopPost**
> PlayStopResponse v01PlayStopPost(callUUID)

/v0.1/PlayStop/

Interrupts media playback on a given call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String callUUID = "callUUID_example"; // String | Unique identifier of the call
    try {
      PlayStopResponse result = apiInstance.v01PlayStopPost(callUUID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01PlayStopPost");
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
| **callUUID** | **String**| Unique identifier of the call | |

### Return type

[**PlayStopResponse**](PlayStopResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01RecordStartPost"></a>
# **v01RecordStartPost**
> RecordStartResponse v01RecordStartPost(callUUID, fileFormat, fileName, filePath, timeLimit)

/v0.1/RecordStart/

Initiates recording of a given call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String callUUID = "callUUID_example"; // String | Unique identifier of the call to be recorded
    String fileFormat = "wav"; // String | File format (extension)
    String fileName = ""; // String | Recording file name (without extension); if empty, a timestamp based file name will be generated
    String filePath = ""; // String | Directory path/URI where the recording file will be saved
    Integer timeLimit = 60; // Integer | Maximum recording length, in seconds
    try {
      RecordStartResponse result = apiInstance.v01RecordStartPost(callUUID, fileFormat, fileName, filePath, timeLimit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01RecordStartPost");
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
| **callUUID** | **String**| Unique identifier of the call to be recorded | [optional] |
| **fileFormat** | **String**| File format (extension) | [optional] [default to mp3] [enum: wav, mp3] |
| **fileName** | **String**| Recording file name (without extension); if empty, a timestamp based file name will be generated | [optional] [default to ] |
| **filePath** | **String**| Directory path/URI where the recording file will be saved | [optional] [default to ] |
| **timeLimit** | **Integer**| Maximum recording length, in seconds | [optional] [default to 60] |

### Return type

[**RecordStartResponse**](RecordStartResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01RecordStopPost"></a>
# **v01RecordStopPost**
> RecordStopResponse v01RecordStopPost(callUUID, recordFile)

/v0.1/RecordStop/

Stops the recording of a given call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String callUUID = "callUUID_example"; // String | Unique identifier of the call
    String recordFile = "recordFile_example"; // String | Full path to recording file, as returned by RecordStart; `all` shorthand is also available
    try {
      RecordStopResponse result = apiInstance.v01RecordStopPost(callUUID, recordFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01RecordStopPost");
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
| **callUUID** | **String**| Unique identifier of the call | |
| **recordFile** | **String**| Full path to recording file, as returned by RecordStart; &#x60;all&#x60; shorthand is also available | |

### Return type

[**RecordStopResponse**](RecordStopResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01ScheduleHangupPost"></a>
# **v01ScheduleHangupPost**
> ScheduleHangupResponse v01ScheduleHangupPost(callUUID, time)

/v0.1/ScheduleHangup/

Schedules a hangup for a specific call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String callUUID = "callUUID_example"; // String | Unique identifier of the call
    Integer time = 56; // Integer | Time (in seconds) after which the call in question will be hung up
    try {
      ScheduleHangupResponse result = apiInstance.v01ScheduleHangupPost(callUUID, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01ScheduleHangupPost");
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
| **callUUID** | **String**| Unique identifier of the call | |
| **time** | **Integer**| Time (in seconds) after which the call in question will be hung up | |

### Return type

[**ScheduleHangupResponse**](ScheduleHangupResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01SchedulePlayPost"></a>
# **v01SchedulePlayPost**
> SchedulePlayResponse v01SchedulePlayPost(callUUID, sounds, time, legs, length, loop, mix)

/v0.1/SchedulePlay/

Schedules media playback for a specific call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String callUUID = "callUUID_example"; // String | Unique identifier of the call to play media into
    String sounds = "sounds_example"; // String | Comma separated list of file paths/URIs to be played
    Integer time = 56; // Integer | Time (in seconds) after which the media will be playedback
    String legs = "aleg"; // String | Call leg(s) for which the media will be played; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.
    Integer length = 3600; // Integer | Maximum amount of time (in seconds) to playback the media
    Boolean loop = false; // Boolean | Loops the media file(s) indefinitely
    Boolean mix = true; // Boolean | Whether the media should be mixed with the call's audio stream
    try {
      SchedulePlayResponse result = apiInstance.v01SchedulePlayPost(callUUID, sounds, time, legs, length, loop, mix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01SchedulePlayPost");
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
| **callUUID** | **String**| Unique identifier of the call to play media into | |
| **sounds** | **String**| Comma separated list of file paths/URIs to be played | |
| **time** | **Integer**| Time (in seconds) after which the media will be playedback | |
| **legs** | **String**| Call leg(s) for which the media will be played; &#x60;aleg&#x60; refers to the initial call leg, &#x60;bleg&#x60; refers to the bridged call leg, if applicable. | [optional] [default to aleg] [enum: aleg, bleg, both] |
| **length** | **Integer**| Maximum amount of time (in seconds) to playback the media | [optional] [default to 3600] |
| **loop** | **Boolean**| Loops the media file(s) indefinitely | [optional] [default to false] |
| **mix** | **Boolean**| Whether the media should be mixed with the call&#39;s audio stream | [optional] [default to true] |

### Return type

[**SchedulePlayResponse**](SchedulePlayResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01SendDigitsPost"></a>
# **v01SendDigitsPost**
> SendDigitsResponse v01SendDigitsPost(callUUID, digits, leg)

/v0.1/SendDigits/

Emits DMTF tones to a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String callUUID = "callUUID_example"; // String | Unique identifier of the call to send DTMF to
    String digits = "digits_example"; // String | DTMF tones to be sent; each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string
    String leg = "aleg"; // String | Call leg(s) to which DTMFs will be sent; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.
    try {
      SendDigitsResponse result = apiInstance.v01SendDigitsPost(callUUID, digits, leg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01SendDigitsPost");
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
| **callUUID** | **String**| Unique identifier of the call to send DTMF to | |
| **digits** | **String**| DTMF tones to be sent; each occurrence of &#x60;w&#x60; implies a 0.5 seconds delay whereas &#x60;W&#x60; will apply a whole second delay. To alter the tone duration (by default, 2000ms), append &#x60;@&#x60; and the length in milliseconds at the end of the string | |
| **leg** | **String**| Call leg(s) to which DTMFs will be sent; &#x60;aleg&#x60; refers to the initial call leg, &#x60;bleg&#x60; refers to the bridged call leg, if applicable. | [optional] [default to aleg] [enum: aleg, bleg, both] |

### Return type

[**SendDigitsResponse**](SendDigitsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01SoundTouchPost"></a>
# **v01SoundTouchPost**
> SoundTouchResponse v01SoundTouchPost(callUUID, audioDirection, pitch, pitchOctaves, pitchSemiTones, rate, tempo)

/v0.1/SoundTouch/

Applies SoundTouch effects to a live call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String callUUID = "callUUID_example"; // String | Unique identifier of the call to send DTMF to
    String audioDirection = "in"; // String | Media stream to be altered, incoming or outgoing
    Float pitch = 1F; // Float | Adjust the pitch
    Float pitchOctaves = 3.4F; // Float | Adjust the pitch in octaves
    Float pitchSemiTones = 3.4F; // Float | Adjust the pitch in semitones
    Float rate = 1F; // Float | Adjust the rate
    Float tempo = 1F; // Float | Adjust the tempo
    try {
      SoundTouchResponse result = apiInstance.v01SoundTouchPost(callUUID, audioDirection, pitch, pitchOctaves, pitchSemiTones, rate, tempo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01SoundTouchPost");
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
| **callUUID** | **String**| Unique identifier of the call to send DTMF to | |
| **audioDirection** | **String**| Media stream to be altered, incoming or outgoing | [optional] [default to out] [enum: in, out] |
| **pitch** | **Float**| Adjust the pitch | [optional] [default to 1] |
| **pitchOctaves** | **Float**| Adjust the pitch in octaves | [optional] |
| **pitchSemiTones** | **Float**| Adjust the pitch in semitones | [optional] |
| **rate** | **Float**| Adjust the rate | [optional] [default to 1] |
| **tempo** | **Float**| Adjust the tempo | [optional] [default to 1] |

### Return type

[**SoundTouchResponse**](SoundTouchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01SoundTouchStopPost"></a>
# **v01SoundTouchStopPost**
> SoundTouchStopResponse v01SoundTouchStopPost(callUUID)

/v0.1/SoundTouchStop/

Removes SoundTouch effects from a given call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String callUUID = "callUUID_example"; // String | Unique identifier of the call
    try {
      SoundTouchStopResponse result = apiInstance.v01SoundTouchStopPost(callUUID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01SoundTouchStopPost");
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
| **callUUID** | **String**| Unique identifier of the call | |

### Return type

[**SoundTouchStopResponse**](SoundTouchStopResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="v01TransferCallPost"></a>
# **v01TransferCallPost**
> TransferCallResponse v01TransferCallPost(callUUID, url)

/v0.1/TransferCall/

Replaces the RestXML flow of a live call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://raw.github.com/rtckit/media/master/eqivo/readme-splash.png");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CallApi apiInstance = new CallApi(defaultClient);
    String callUUID = "callUUID_example"; // String | Unique identifier of the call
    String url = "url_example"; // String | Absolute URL which will return the updated RestXML flow
    try {
      TransferCallResponse result = apiInstance.v01TransferCallPost(callUUID, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallApi#v01TransferCallPost");
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
| **callUUID** | **String**| Unique identifier of the call | |
| **url** | **String**| Absolute URL which will return the updated RestXML flow | |

### Return type

[**TransferCallResponse**](TransferCallResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

