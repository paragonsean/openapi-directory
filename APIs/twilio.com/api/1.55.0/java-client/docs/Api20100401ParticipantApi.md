# Api20100401ParticipantApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createParticipant**](Api20100401ParticipantApi.md#createParticipant) | **POST** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json |  |
| [**deleteParticipant**](Api20100401ParticipantApi.md#deleteParticipant) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json |  |
| [**fetchParticipant**](Api20100401ParticipantApi.md#fetchParticipant) | **GET** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json |  |
| [**listParticipant**](Api20100401ParticipantApi.md#listParticipant) | **GET** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json |  |
| [**updateParticipant**](Api20100401ParticipantApi.md#updateParticipant) | **POST** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json |  |


<a id="createParticipant"></a>
# **createParticipant**
> ApiV2010AccountConferenceParticipant createParticipant(accountSid, conferenceSid, from, to, amdStatusCallback, amdStatusCallbackMethod, beep, byoc, callReason, callSidToCoach, callToken, callerId, coaching, conferenceRecord, conferenceRecordingStatusCallback, conferenceRecordingStatusCallbackEvent, conferenceRecordingStatusCallbackMethod, conferenceStatusCallback, conferenceStatusCallbackEvent, conferenceStatusCallbackMethod, conferenceTrim, earlyMedia, endConferenceOnExit, jitterBufferSize, label, machineDetection, machineDetectionSilenceTimeout, machineDetectionSpeechEndThreshold, machineDetectionSpeechThreshold, machineDetectionTimeout, maxParticipants, muted, record, recordingChannels, recordingStatusCallback, recordingStatusCallbackEvent, recordingStatusCallbackMethod, recordingTrack, region, sipAuthPassword, sipAuthUsername, startConferenceOnEnter, statusCallback, statusCallbackEvent, statusCallbackMethod, timeLimit, timeout, trim, waitMethod, waitUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ParticipantApi apiInstance = new Api20100401ParticipantApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    String conferenceSid = "conferenceSid_example"; // String | The SID of the participant's conference.
    String from = "from_example"; // String | The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). Client identifiers are formatted `client:name`. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the `to` parameter is a phone number, `from` must also be a phone number. If `to` is sip address, this value of `from` should be a username portion to be used to populate the P-Asserted-Identity header that is passed to the SIP endpoint.
    String to = "to_example"; // String | The phone number, SIP address, or Client identifier that received this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). SIP addresses are formatted as `sip:name@company.com`. Client identifiers are formatted `client:name`. [Custom parameters](https://www.twilio.com/docs/voice/api/conference-participant-resource#custom-parameters) may also be specified.
    URI amdStatusCallback = new URI(); // URI | The URL that we should call using the `amd_status_callback_method` to notify customer application whether the call was answered by human, machine or fax.
    String amdStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use when calling the `amd_status_callback` URL. Can be: `GET` or `POST` and the default is `POST`.
    String beep = "beep_example"; // String | Whether to play a notification beep to the conference when the participant joins. Can be: `true`, `false`, `onEnter`, or `onExit`. The default value is `true`.
    String byoc = "byoc_example"; // String | The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that `byoc` is only meaningful when `to` is a phone number; it will otherwise be ignored. (Beta)
    String callReason = "callReason_example"; // String | The Reason for the outgoing call. Use it to specify the purpose of the call that is presented on the called party's phone. (Branded Calls Beta)
    String callSidToCoach = "callSidToCoach_example"; // String | The SID of the participant who is being `coached`. The participant being coached is the only participant who can hear the participant who is `coaching`.
    String callToken = "callToken_example"; // String | A token string needed to invoke a forwarded call. A call_token is generated when an incoming call is received on a Twilio number. Pass an incoming call's call_token value to a forwarded call via the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the original incoming call.
    String callerId = "callerId_example"; // String | The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). Client identifiers are formatted `client:name`. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the `to` parameter is a phone number, `callerId` must also be a phone number. If `to` is sip address, this value of `callerId` should be a username portion to be used to populate the From header that is passed to the SIP endpoint.
    Boolean coaching = true; // Boolean | Whether the participant is coaching another call. Can be: `true` or `false`. If not present, defaults to `false` unless `call_sid_to_coach` is defined. If `true`, `call_sid_to_coach` must be defined.
    String conferenceRecord = "conferenceRecord_example"; // String | Whether to record the conference the participant is joining. Can be: `true`, `false`, `record-from-start`, and `do-not-record`. The default value is `false`.
    URI conferenceRecordingStatusCallback = new URI(); // URI | The URL we should call using the `conference_recording_status_callback_method` when the conference recording is available.
    List<String> conferenceRecordingStatusCallbackEvent = Arrays.asList(); // List<String> | The conference recording state changes that generate a call to `conference_recording_status_callback`. Can be: `in-progress`, `completed`, `failed`, and `absent`. Separate multiple values with a space, ex: `'in-progress completed failed'`
    String conferenceRecordingStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `conference_recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    URI conferenceStatusCallback = new URI(); // URI | The URL we should call using the `conference_status_callback_method` when the conference events in `conference_status_callback_event` occur. Only the value set by the first participant to join the conference is used. Subsequent `conference_status_callback` values are ignored.
    List<String> conferenceStatusCallbackEvent = Arrays.asList(); // List<String> | The conference state changes that should generate a call to `conference_status_callback`. Can be: `start`, `end`, `join`, `leave`, `mute`, `hold`, `modify`, `speaker`, and `announcement`. Separate multiple values with a space. Defaults to `start end`.
    String conferenceStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `conference_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    String conferenceTrim = "conferenceTrim_example"; // String | Whether to trim leading and trailing silence from the conference recording. Can be: `trim-silence` or `do-not-trim` and defaults to `trim-silence`.
    Boolean earlyMedia = true; // Boolean | Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. Can be: `true` or `false` and defaults to `true`.
    Boolean endConferenceOnExit = true; // Boolean | Whether to end the conference when the participant leaves. Can be: `true` or `false` and defaults to `false`.
    String jitterBufferSize = "jitterBufferSize_example"; // String | Jitter buffer size for the connecting participant. Twilio will use this setting to apply Jitter Buffer before participant's audio is mixed into the conference. Can be: `off`, `small`, `medium`, and `large`. Default to `large`.
    String label = "label_example"; // String | A label for this participant. If one is supplied, it may subsequently be used to fetch, update or delete the participant.
    String machineDetection = "machineDetection_example"; // String | Whether to detect if a human, answering machine, or fax has picked up the call. Can be: `Enable` or `DetectMessageEnd`. Use `Enable` if you would like us to return `AnsweredBy` as soon as the called party is identified. Use `DetectMessageEnd`, if you would like to leave a message on an answering machine. For more information, see [Answering Machine Detection](https://www.twilio.com/docs/voice/answering-machine-detection).
    Integer machineDetectionSilenceTimeout = 56; // Integer | The number of milliseconds of initial silence after which an `unknown` AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000.
    Integer machineDetectionSpeechEndThreshold = 56; // Integer | The number of milliseconds of silence after speech activity at which point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200.
    Integer machineDetectionSpeechThreshold = 56; // Integer | The number of milliseconds that is used as the measuring stick for the length of the speech activity, where durations lower than this value will be interpreted as a human and longer than this value as a machine. Possible Values: 1000-6000. Default: 2400.
    Integer machineDetectionTimeout = 56; // Integer | The number of seconds that we should attempt to detect an answering machine before timing out and sending a voice request with `AnsweredBy` of `unknown`. The default timeout is 30 seconds.
    Integer maxParticipants = 56; // Integer | The maximum number of participants in the conference. Can be a positive integer from `2` to `250`. The default value is `250`.
    Boolean muted = true; // Boolean | Whether the agent is muted in the conference. Can be `true` or `false` and the default is `false`.
    Boolean record = true; // Boolean | Whether to record the participant and their conferences, including the time between conferences. Can be `true` or `false` and the default is `false`.
    String recordingChannels = "recordingChannels_example"; // String | The recording channels for the final recording. Can be: `mono` or `dual` and the default is `mono`.
    URI recordingStatusCallback = new URI(); // URI | The URL that we should call using the `recording_status_callback_method` when the recording status changes.
    List<String> recordingStatusCallbackEvent = Arrays.asList(); // List<String> | The recording state changes that should generate a call to `recording_status_callback`. Can be: `started`, `in-progress`, `paused`, `resumed`, `stopped`, `completed`, `failed`, and `absent`. Separate multiple values with a space, ex: `'in-progress completed failed'`.
    String recordingStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use when we call `recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    String recordingTrack = "recordingTrack_example"; // String | The audio track to record for the call. Can be: `inbound`, `outbound` or `both`. The default is `both`. `inbound` records the audio that is received by Twilio. `outbound` records the audio that is sent from Twilio. `both` records the audio that is received and sent by Twilio.
    String region = "region_example"; // String | The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:`us1`, `ie1`, `de1`, `sg1`, `br1`, `au1`, or `jp1`.
    String sipAuthPassword = "sipAuthPassword_example"; // String | The SIP password for authentication.
    String sipAuthUsername = "sipAuthUsername_example"; // String | The SIP username used for authentication.
    Boolean startConferenceOnEnter = true; // Boolean | Whether to start the conference when the participant joins, if it has not already started. Can be: `true` or `false` and the default is `true`. If `false` and the conference has not started, the participant is muted and hears background music until another participant starts the conference.
    URI statusCallback = new URI(); // URI | The URL we should call using the `status_callback_method` to send status information to your application.
    List<String> statusCallbackEvent = Arrays.asList(); // List<String> | The conference state changes that should generate a call to `status_callback`. Can be: `initiated`, `ringing`, `answered`, and `completed`. Separate multiple values with a space. The default value is `completed`.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback`. Can be: `GET` and `POST` and defaults to `POST`.
    Integer timeLimit = 56; // Integer | The maximum duration of the call in seconds. Constraints depend on account and configuration.
    Integer timeout = 56; // Integer | The number of seconds that we should allow the phone to ring before assuming there is no answer. Can be an integer between `5` and `600`, inclusive. The default value is `60`. We always add a 5-second timeout buffer to outgoing calls, so  value of 10 would result in an actual timeout that was closer to 15 seconds.
    String trim = "trim_example"; // String | Whether to trim any leading and trailing silence from the participant recording. Can be: `trim-silence` or `do-not-trim` and the default is `trim-silence`.
    String waitMethod = "HEAD"; // String | The HTTP method we should use to call `wait_url`. Can be `GET` or `POST` and the default is `POST`. When using a static audio file, this should be `GET` so that we can cache the file.
    URI waitUrl = new URI(); // URI | The URL we should call using the `wait_method` for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic).
    try {
      ApiV2010AccountConferenceParticipant result = apiInstance.createParticipant(accountSid, conferenceSid, from, to, amdStatusCallback, amdStatusCallbackMethod, beep, byoc, callReason, callSidToCoach, callToken, callerId, coaching, conferenceRecord, conferenceRecordingStatusCallback, conferenceRecordingStatusCallbackEvent, conferenceRecordingStatusCallbackMethod, conferenceStatusCallback, conferenceStatusCallbackEvent, conferenceStatusCallbackMethod, conferenceTrim, earlyMedia, endConferenceOnExit, jitterBufferSize, label, machineDetection, machineDetectionSilenceTimeout, machineDetectionSpeechEndThreshold, machineDetectionSpeechThreshold, machineDetectionTimeout, maxParticipants, muted, record, recordingChannels, recordingStatusCallback, recordingStatusCallbackEvent, recordingStatusCallbackMethod, recordingTrack, region, sipAuthPassword, sipAuthUsername, startConferenceOnEnter, statusCallback, statusCallbackEvent, statusCallbackMethod, timeLimit, timeout, trim, waitMethod, waitUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ParticipantApi#createParticipant");
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
| **conferenceSid** | **String**| The SID of the participant&#39;s conference. | |
| **from** | **String**| The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). Client identifiers are formatted &#x60;client:name&#x60;. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the &#x60;to&#x60; parameter is a phone number, &#x60;from&#x60; must also be a phone number. If &#x60;to&#x60; is sip address, this value of &#x60;from&#x60; should be a username portion to be used to populate the P-Asserted-Identity header that is passed to the SIP endpoint. | |
| **to** | **String**| The phone number, SIP address, or Client identifier that received this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). SIP addresses are formatted as &#x60;sip:name@company.com&#x60;. Client identifiers are formatted &#x60;client:name&#x60;. [Custom parameters](https://www.twilio.com/docs/voice/api/conference-participant-resource#custom-parameters) may also be specified. | |
| **amdStatusCallback** | **URI**| The URL that we should call using the &#x60;amd_status_callback_method&#x60; to notify customer application whether the call was answered by human, machine or fax. | [optional] |
| **amdStatusCallbackMethod** | **String**| The HTTP method we should use when calling the &#x60;amd_status_callback&#x60; URL. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **beep** | **String**| Whether to play a notification beep to the conference when the participant joins. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;onEnter&#x60;, or &#x60;onExit&#x60;. The default value is &#x60;true&#x60;. | [optional] |
| **byoc** | **String**| The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that &#x60;byoc&#x60; is only meaningful when &#x60;to&#x60; is a phone number; it will otherwise be ignored. (Beta) | [optional] |
| **callReason** | **String**| The Reason for the outgoing call. Use it to specify the purpose of the call that is presented on the called party&#39;s phone. (Branded Calls Beta) | [optional] |
| **callSidToCoach** | **String**| The SID of the participant who is being &#x60;coached&#x60;. The participant being coached is the only participant who can hear the participant who is &#x60;coaching&#x60;. | [optional] |
| **callToken** | **String**| A token string needed to invoke a forwarded call. A call_token is generated when an incoming call is received on a Twilio number. Pass an incoming call&#39;s call_token value to a forwarded call via the call_token parameter when creating a new call. A forwarded call should bear the same CallerID of the original incoming call. | [optional] |
| **callerId** | **String**| The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). Client identifiers are formatted &#x60;client:name&#x60;. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the &#x60;to&#x60; parameter is a phone number, &#x60;callerId&#x60; must also be a phone number. If &#x60;to&#x60; is sip address, this value of &#x60;callerId&#x60; should be a username portion to be used to populate the From header that is passed to the SIP endpoint. | [optional] |
| **coaching** | **Boolean**| Whether the participant is coaching another call. Can be: &#x60;true&#x60; or &#x60;false&#x60;. If not present, defaults to &#x60;false&#x60; unless &#x60;call_sid_to_coach&#x60; is defined. If &#x60;true&#x60;, &#x60;call_sid_to_coach&#x60; must be defined. | [optional] |
| **conferenceRecord** | **String**| Whether to record the conference the participant is joining. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;record-from-start&#x60;, and &#x60;do-not-record&#x60;. The default value is &#x60;false&#x60;. | [optional] |
| **conferenceRecordingStatusCallback** | **URI**| The URL we should call using the &#x60;conference_recording_status_callback_method&#x60; when the conference recording is available. | [optional] |
| **conferenceRecordingStatusCallbackEvent** | [**List&lt;String&gt;**](String.md)| The conference recording state changes that generate a call to &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;in-progress&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, and &#x60;absent&#x60;. Separate multiple values with a space, ex: &#x60;&#39;in-progress completed failed&#39;&#x60; | [optional] |
| **conferenceRecordingStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **conferenceStatusCallback** | **URI**| The URL we should call using the &#x60;conference_status_callback_method&#x60; when the conference events in &#x60;conference_status_callback_event&#x60; occur. Only the value set by the first participant to join the conference is used. Subsequent &#x60;conference_status_callback&#x60; values are ignored. | [optional] |
| **conferenceStatusCallbackEvent** | [**List&lt;String&gt;**](String.md)| The conference state changes that should generate a call to &#x60;conference_status_callback&#x60;. Can be: &#x60;start&#x60;, &#x60;end&#x60;, &#x60;join&#x60;, &#x60;leave&#x60;, &#x60;mute&#x60;, &#x60;hold&#x60;, &#x60;modify&#x60;, &#x60;speaker&#x60;, and &#x60;announcement&#x60;. Separate multiple values with a space. Defaults to &#x60;start end&#x60;. | [optional] |
| **conferenceStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;conference_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **conferenceTrim** | **String**| Whether to trim leading and trailing silence from the conference recording. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and defaults to &#x60;trim-silence&#x60;. | [optional] |
| **earlyMedia** | **Boolean**| Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;true&#x60;. | [optional] |
| **endConferenceOnExit** | **Boolean**| Whether to end the conference when the participant leaves. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional] |
| **jitterBufferSize** | **String**| Jitter buffer size for the connecting participant. Twilio will use this setting to apply Jitter Buffer before participant&#39;s audio is mixed into the conference. Can be: &#x60;off&#x60;, &#x60;small&#x60;, &#x60;medium&#x60;, and &#x60;large&#x60;. Default to &#x60;large&#x60;. | [optional] |
| **label** | **String**| A label for this participant. If one is supplied, it may subsequently be used to fetch, update or delete the participant. | [optional] |
| **machineDetection** | **String**| Whether to detect if a human, answering machine, or fax has picked up the call. Can be: &#x60;Enable&#x60; or &#x60;DetectMessageEnd&#x60;. Use &#x60;Enable&#x60; if you would like us to return &#x60;AnsweredBy&#x60; as soon as the called party is identified. Use &#x60;DetectMessageEnd&#x60;, if you would like to leave a message on an answering machine. For more information, see [Answering Machine Detection](https://www.twilio.com/docs/voice/answering-machine-detection). | [optional] |
| **machineDetectionSilenceTimeout** | **Integer**| The number of milliseconds of initial silence after which an &#x60;unknown&#x60; AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000. | [optional] |
| **machineDetectionSpeechEndThreshold** | **Integer**| The number of milliseconds of silence after speech activity at which point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200. | [optional] |
| **machineDetectionSpeechThreshold** | **Integer**| The number of milliseconds that is used as the measuring stick for the length of the speech activity, where durations lower than this value will be interpreted as a human and longer than this value as a machine. Possible Values: 1000-6000. Default: 2400. | [optional] |
| **machineDetectionTimeout** | **Integer**| The number of seconds that we should attempt to detect an answering machine before timing out and sending a voice request with &#x60;AnsweredBy&#x60; of &#x60;unknown&#x60;. The default timeout is 30 seconds. | [optional] |
| **maxParticipants** | **Integer**| The maximum number of participants in the conference. Can be a positive integer from &#x60;2&#x60; to &#x60;250&#x60;. The default value is &#x60;250&#x60;. | [optional] |
| **muted** | **Boolean**| Whether the agent is muted in the conference. Can be &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] |
| **record** | **Boolean**| Whether to record the participant and their conferences, including the time between conferences. Can be &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] |
| **recordingChannels** | **String**| The recording channels for the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60; and the default is &#x60;mono&#x60;. | [optional] |
| **recordingStatusCallback** | **URI**| The URL that we should call using the &#x60;recording_status_callback_method&#x60; when the recording status changes. | [optional] |
| **recordingStatusCallbackEvent** | [**List&lt;String&gt;**](String.md)| The recording state changes that should generate a call to &#x60;recording_status_callback&#x60;. Can be: &#x60;started&#x60;, &#x60;in-progress&#x60;, &#x60;paused&#x60;, &#x60;resumed&#x60;, &#x60;stopped&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, and &#x60;absent&#x60;. Separate multiple values with a space, ex: &#x60;&#39;in-progress completed failed&#39;&#x60;. | [optional] |
| **recordingStatusCallbackMethod** | **String**| The HTTP method we should use when we call &#x60;recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **recordingTrack** | **String**| The audio track to record for the call. Can be: &#x60;inbound&#x60;, &#x60;outbound&#x60; or &#x60;both&#x60;. The default is &#x60;both&#x60;. &#x60;inbound&#x60; records the audio that is received by Twilio. &#x60;outbound&#x60; records the audio that is sent from Twilio. &#x60;both&#x60; records the audio that is received and sent by Twilio. | [optional] |
| **region** | **String**| The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:&#x60;us1&#x60;, &#x60;ie1&#x60;, &#x60;de1&#x60;, &#x60;sg1&#x60;, &#x60;br1&#x60;, &#x60;au1&#x60;, or &#x60;jp1&#x60;. | [optional] |
| **sipAuthPassword** | **String**| The SIP password for authentication. | [optional] |
| **sipAuthUsername** | **String**| The SIP username used for authentication. | [optional] |
| **startConferenceOnEnter** | **Boolean**| Whether to start the conference when the participant joins, if it has not already started. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If &#x60;false&#x60; and the conference has not started, the participant is muted and hears background music until another participant starts the conference. | [optional] |
| **statusCallback** | **URI**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] |
| **statusCallbackEvent** | [**List&lt;String&gt;**](String.md)| The conference state changes that should generate a call to &#x60;status_callback&#x60;. Can be: &#x60;initiated&#x60;, &#x60;ringing&#x60;, &#x60;answered&#x60;, and &#x60;completed&#x60;. Separate multiple values with a space. The default value is &#x60;completed&#x60;. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; and &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **timeLimit** | **Integer**| The maximum duration of the call in seconds. Constraints depend on account and configuration. | [optional] |
| **timeout** | **Integer**| The number of seconds that we should allow the phone to ring before assuming there is no answer. Can be an integer between &#x60;5&#x60; and &#x60;600&#x60;, inclusive. The default value is &#x60;60&#x60;. We always add a 5-second timeout buffer to outgoing calls, so  value of 10 would result in an actual timeout that was closer to 15 seconds. | [optional] |
| **trim** | **String**| Whether to trim any leading and trailing silence from the participant recording. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and the default is &#x60;trim-silence&#x60;. | [optional] |
| **waitMethod** | **String**| The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **waitUrl** | **URI**| The URL we should call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic). | [optional] |

### Return type

[**ApiV2010AccountConferenceParticipant**](ApiV2010AccountConferenceParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteParticipant"></a>
# **deleteParticipant**
> deleteParticipant(accountSid, conferenceSid, callSid)



Kick a participant from a given conference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ParticipantApi apiInstance = new Api20100401ParticipantApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to delete.
    String conferenceSid = "conferenceSid_example"; // String | The SID of the conference with the participants to delete.
    String callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to delete. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.
    try {
      apiInstance.deleteParticipant(accountSid, conferenceSid, callSid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ParticipantApi#deleteParticipant");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to delete. | |
| **conferenceSid** | **String**| The SID of the conference with the participants to delete. | |
| **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to delete. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20. | |

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

<a id="fetchParticipant"></a>
# **fetchParticipant**
> ApiV2010AccountConferenceParticipant fetchParticipant(accountSid, conferenceSid, callSid)



Fetch an instance of a participant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ParticipantApi apiInstance = new Api20100401ParticipantApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resource to fetch.
    String conferenceSid = "conferenceSid_example"; // String | The SID of the conference with the participant to fetch.
    String callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to fetch. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.
    try {
      ApiV2010AccountConferenceParticipant result = apiInstance.fetchParticipant(accountSid, conferenceSid, callSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ParticipantApi#fetchParticipant");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resource to fetch. | |
| **conferenceSid** | **String**| The SID of the conference with the participant to fetch. | |
| **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to fetch. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20. | |

### Return type

[**ApiV2010AccountConferenceParticipant**](ApiV2010AccountConferenceParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listParticipant"></a>
# **listParticipant**
> ListParticipantResponse listParticipant(accountSid, conferenceSid, muted, hold, coaching, pageSize, page, pageToken)



Retrieve a list of participants belonging to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ParticipantApi apiInstance = new Api20100401ParticipantApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to read.
    String conferenceSid = "conferenceSid_example"; // String | The SID of the conference with the participants to read.
    Boolean muted = true; // Boolean | Whether to return only participants that are muted. Can be: `true` or `false`.
    Boolean hold = true; // Boolean | Whether to return only participants that are on hold. Can be: `true` or `false`.
    Boolean coaching = true; // Boolean | Whether to return only participants who are coaching another call. Can be: `true` or `false`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListParticipantResponse result = apiInstance.listParticipant(accountSid, conferenceSid, muted, hold, coaching, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ParticipantApi#listParticipant");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to read. | |
| **conferenceSid** | **String**| The SID of the conference with the participants to read. | |
| **muted** | **Boolean**| Whether to return only participants that are muted. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **hold** | **Boolean**| Whether to return only participants that are on hold. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **coaching** | **Boolean**| Whether to return only participants who are coaching another call. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListParticipantResponse**](ListParticipantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateParticipant"></a>
# **updateParticipant**
> ApiV2010AccountConferenceParticipant updateParticipant(accountSid, conferenceSid, callSid, announceMethod, announceUrl, beepOnExit, callSidToCoach, coaching, endConferenceOnExit, hold, holdMethod, holdUrl, muted, waitMethod, waitUrl)



Update the properties of the participant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401ParticipantApi apiInstance = new Api20100401ParticipantApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to update.
    String conferenceSid = "conferenceSid_example"; // String | The SID of the conference with the participant to update.
    String callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to update. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.
    String announceMethod = "HEAD"; // String | The HTTP method we should use to call `announce_url`. Can be: `GET` or `POST` and defaults to `POST`.
    URI announceUrl = new URI(); // URI | The URL we call using the `announce_method` for an announcement to the participant. The URL may return an MP3 file, a WAV file, or a TwiML document that contains `<Play>`, `<Say>`, `<Pause>`, or `<Redirect>` verbs.
    Boolean beepOnExit = true; // Boolean | Whether to play a notification beep to the conference when the participant exits. Can be: `true` or `false`.
    String callSidToCoach = "callSidToCoach_example"; // String | The SID of the participant who is being `coached`. The participant being coached is the only participant who can hear the participant who is `coaching`.
    Boolean coaching = true; // Boolean | Whether the participant is coaching another call. Can be: `true` or `false`. If not present, defaults to `false` unless `call_sid_to_coach` is defined. If `true`, `call_sid_to_coach` must be defined.
    Boolean endConferenceOnExit = true; // Boolean | Whether to end the conference when the participant leaves. Can be: `true` or `false` and defaults to `false`.
    Boolean hold = true; // Boolean | Whether the participant should be on hold. Can be: `true` or `false`. `true` puts the participant on hold, and `false` lets them rejoin the conference.
    String holdMethod = "HEAD"; // String | The HTTP method we should use to call `hold_url`. Can be: `GET` or `POST` and the default is `GET`.
    URI holdUrl = new URI(); // URI | The URL we call using the `hold_method` for music that plays when the participant is on hold. The URL may return an MP3 file, a WAV file, or a TwiML document that contains `<Play>`, `<Say>`, `<Pause>`, or `<Redirect>` verbs.
    Boolean muted = true; // Boolean | Whether the participant should be muted. Can be `true` or `false`. `true` will mute the participant, and `false` will un-mute them. Anything value other than `true` or `false` is interpreted as `false`.
    String waitMethod = "HEAD"; // String | The HTTP method we should use to call `wait_url`. Can be `GET` or `POST` and the default is `POST`. When using a static audio file, this should be `GET` so that we can cache the file.
    URI waitUrl = new URI(); // URI | The URL we call using the `wait_method` for the music to play while participants are waiting for the conference to start. The URL may return an MP3 file, a WAV file, or a TwiML document that contains `<Play>`, `<Say>`, `<Pause>`, or `<Redirect>` verbs. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic).
    try {
      ApiV2010AccountConferenceParticipant result = apiInstance.updateParticipant(accountSid, conferenceSid, callSid, announceMethod, announceUrl, beepOnExit, callSidToCoach, coaching, endConferenceOnExit, hold, holdMethod, holdUrl, muted, waitMethod, waitUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401ParticipantApi#updateParticipant");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to update. | |
| **conferenceSid** | **String**| The SID of the conference with the participant to update. | |
| **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to update. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20. | |
| **announceMethod** | **String**| The HTTP method we should use to call &#x60;announce_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **announceUrl** | **URI**| The URL we call using the &#x60;announce_method&#x60; for an announcement to the participant. The URL may return an MP3 file, a WAV file, or a TwiML document that contains &#x60;&lt;Play&gt;&#x60;, &#x60;&lt;Say&gt;&#x60;, &#x60;&lt;Pause&gt;&#x60;, or &#x60;&lt;Redirect&gt;&#x60; verbs. | [optional] |
| **beepOnExit** | **Boolean**| Whether to play a notification beep to the conference when the participant exits. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **callSidToCoach** | **String**| The SID of the participant who is being &#x60;coached&#x60;. The participant being coached is the only participant who can hear the participant who is &#x60;coaching&#x60;. | [optional] |
| **coaching** | **Boolean**| Whether the participant is coaching another call. Can be: &#x60;true&#x60; or &#x60;false&#x60;. If not present, defaults to &#x60;false&#x60; unless &#x60;call_sid_to_coach&#x60; is defined. If &#x60;true&#x60;, &#x60;call_sid_to_coach&#x60; must be defined. | [optional] |
| **endConferenceOnExit** | **Boolean**| Whether to end the conference when the participant leaves. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional] |
| **hold** | **Boolean**| Whether the participant should be on hold. Can be: &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; puts the participant on hold, and &#x60;false&#x60; lets them rejoin the conference. | [optional] |
| **holdMethod** | **String**| The HTTP method we should use to call &#x60;hold_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;GET&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **holdUrl** | **URI**| The URL we call using the &#x60;hold_method&#x60; for music that plays when the participant is on hold. The URL may return an MP3 file, a WAV file, or a TwiML document that contains &#x60;&lt;Play&gt;&#x60;, &#x60;&lt;Say&gt;&#x60;, &#x60;&lt;Pause&gt;&#x60;, or &#x60;&lt;Redirect&gt;&#x60; verbs. | [optional] |
| **muted** | **Boolean**| Whether the participant should be muted. Can be &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; will mute the participant, and &#x60;false&#x60; will un-mute them. Anything value other than &#x60;true&#x60; or &#x60;false&#x60; is interpreted as &#x60;false&#x60;. | [optional] |
| **waitMethod** | **String**| The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **waitUrl** | **URI**| The URL we call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The URL may return an MP3 file, a WAV file, or a TwiML document that contains &#x60;&lt;Play&gt;&#x60;, &#x60;&lt;Say&gt;&#x60;, &#x60;&lt;Pause&gt;&#x60;, or &#x60;&lt;Redirect&gt;&#x60; verbs. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic). | [optional] |

### Return type

[**ApiV2010AccountConferenceParticipant**](ApiV2010AccountConferenceParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

