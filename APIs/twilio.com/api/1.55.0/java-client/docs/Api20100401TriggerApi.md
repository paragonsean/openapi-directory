# Api20100401TriggerApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUsageTrigger**](Api20100401TriggerApi.md#createUsageTrigger) | **POST** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json |  |
| [**deleteUsageTrigger**](Api20100401TriggerApi.md#deleteUsageTrigger) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json |  |
| [**fetchUsageTrigger**](Api20100401TriggerApi.md#fetchUsageTrigger) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json |  |
| [**listUsageTrigger**](Api20100401TriggerApi.md#listUsageTrigger) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json |  |
| [**updateUsageTrigger**](Api20100401TriggerApi.md#updateUsageTrigger) | **POST** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json |  |


<a id="createUsageTrigger"></a>
# **createUsageTrigger**
> ApiV2010AccountUsageUsageTrigger createUsageTrigger(accountSid, callbackUrl, triggerValue, usageCategory, callbackMethod, friendlyName, recurring, triggerBy)



Create a new UsageTrigger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401TriggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401TriggerApi apiInstance = new Api20100401TriggerApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    URI callbackUrl = new URI(); // URI | The URL we should call using `callback_method` when the trigger fires.
    String triggerValue = "triggerValue_example"; // String | The usage value at which the trigger should fire.  For convenience, you can use an offset value such as `+30` to specify a trigger_value that is 30 units more than the current usage value. Be sure to urlencode a `+` as `%2B`.
    UsageTriggerEnumUsageCategory usageCategory = UsageTriggerEnumUsageCategory.fromValue("a2p-registration-fees"); // UsageTriggerEnumUsageCategory | 
    String callbackMethod = "HEAD"; // String | The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is `POST`.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    UsageTriggerEnumRecurring recurring = UsageTriggerEnumRecurring.fromValue("daily"); // UsageTriggerEnumRecurring | 
    UsageTriggerEnumTriggerField triggerBy = UsageTriggerEnumTriggerField.fromValue("count"); // UsageTriggerEnumTriggerField | 
    try {
      ApiV2010AccountUsageUsageTrigger result = apiInstance.createUsageTrigger(accountSid, callbackUrl, triggerValue, usageCategory, callbackMethod, friendlyName, recurring, triggerBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401TriggerApi#createUsageTrigger");
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
| **callbackUrl** | **URI**| The URL we should call using &#x60;callback_method&#x60; when the trigger fires. | |
| **triggerValue** | **String**| The usage value at which the trigger should fire.  For convenience, you can use an offset value such as &#x60;+30&#x60; to specify a trigger_value that is 30 units more than the current usage value. Be sure to urlencode a &#x60;+&#x60; as &#x60;%2B&#x60;. | |
| **usageCategory** | **UsageTriggerEnumUsageCategory**|  | [enum: a2p-registration-fees, agent-conference, amazon-polly, answering-machine-detection, authy-authentications, authy-calls-outbound, authy-monthly-fees, authy-phone-intelligence, authy-phone-verifications, authy-sms-outbound, call-progess-events, calleridlookups, calls, calls-client, calls-globalconference, calls-inbound, calls-inbound-local, calls-inbound-mobile, calls-inbound-tollfree, calls-outbound, calls-pay-verb-transactions, calls-recordings, calls-sip, calls-sip-inbound, calls-sip-outbound, calls-transfers, carrier-lookups, conversations, conversations-api-requests, conversations-conversation-events, conversations-endpoint-connectivity, conversations-events, conversations-participant-events, conversations-participants, cps, flex-usage, fraud-lookups, group-rooms, group-rooms-data-track, group-rooms-encrypted-media-recorded, group-rooms-media-downloaded, group-rooms-media-recorded, group-rooms-media-routed, group-rooms-media-stored, group-rooms-participant-minutes, group-rooms-recorded-minutes, imp-v1-usage, lookups, marketplace, marketplace-algorithmia-named-entity-recognition, marketplace-cadence-transcription, marketplace-cadence-translation, marketplace-capio-speech-to-text, marketplace-convriza-ababa, marketplace-deepgram-phrase-detector, marketplace-digital-segment-business-info, marketplace-facebook-offline-conversions, marketplace-google-speech-to-text, marketplace-ibm-watson-message-insights, marketplace-ibm-watson-message-sentiment, marketplace-ibm-watson-recording-analysis, marketplace-ibm-watson-tone-analyzer, marketplace-icehook-systems-scout, marketplace-infogroup-dataaxle-bizinfo, marketplace-keen-io-contact-center-analytics, marketplace-marchex-cleancall, marketplace-marchex-sentiment-analysis-for-sms, marketplace-marketplace-nextcaller-social-id, marketplace-mobile-commons-opt-out-classifier, marketplace-nexiwave-voicemail-to-text, marketplace-nextcaller-advanced-caller-identification, marketplace-nomorobo-spam-score, marketplace-payfone-tcpa-compliance, marketplace-remeeting-automatic-speech-recognition, marketplace-tcpa-defense-solutions-blacklist-feed, marketplace-telo-opencnam, marketplace-truecnam-true-spam, marketplace-twilio-caller-name-lookup-us, marketplace-twilio-carrier-information-lookup, marketplace-voicebase-pci, marketplace-voicebase-transcription, marketplace-voicebase-transcription-custom-vocabulary, marketplace-whitepages-pro-caller-identification, marketplace-whitepages-pro-phone-intelligence, marketplace-whitepages-pro-phone-reputation, marketplace-wolfarm-spoken-results, marketplace-wolfram-short-answer, marketplace-ytica-contact-center-reporting-analytics, mediastorage, mms, mms-inbound, mms-inbound-longcode, mms-inbound-shortcode, mms-messages-carrierfees, mms-outbound, mms-outbound-longcode, mms-outbound-shortcode, monitor-reads, monitor-storage, monitor-writes, notify, notify-actions-attempts, notify-channels, number-format-lookups, pchat, pchat-users, peer-to-peer-rooms-participant-minutes, pfax, pfax-minutes, pfax-minutes-inbound, pfax-minutes-outbound, pfax-pages, phonenumbers, phonenumbers-cps, phonenumbers-emergency, phonenumbers-local, phonenumbers-mobile, phonenumbers-setups, phonenumbers-tollfree, premiumsupport, proxy, proxy-active-sessions, pstnconnectivity, pv, pv-composition-media-downloaded, pv-composition-media-encrypted, pv-composition-media-stored, pv-composition-minutes, pv-recording-compositions, pv-room-participants, pv-room-participants-au1, pv-room-participants-br1, pv-room-participants-ie1, pv-room-participants-jp1, pv-room-participants-sg1, pv-room-participants-us1, pv-room-participants-us2, pv-rooms, pv-sip-endpoint-registrations, recordings, recordingstorage, rooms-group-bandwidth, rooms-group-minutes, rooms-peer-to-peer-minutes, shortcodes, shortcodes-customerowned, shortcodes-mms-enablement, shortcodes-mps, shortcodes-random, shortcodes-uk, shortcodes-vanity, small-group-rooms, small-group-rooms-data-track, small-group-rooms-participant-minutes, sms, sms-inbound, sms-inbound-longcode, sms-inbound-shortcode, sms-messages-carrierfees, sms-messages-features, sms-messages-features-senderid, sms-outbound, sms-outbound-content-inspection, sms-outbound-longcode, sms-outbound-shortcode, speech-recognition, studio-engagements, sync, sync-actions, sync-endpoint-hours, sync-endpoint-hours-above-daily-cap, taskrouter-tasks, totalprice, transcriptions, trunking-cps, trunking-emergency-calls, trunking-origination, trunking-origination-local, trunking-origination-mobile, trunking-origination-tollfree, trunking-recordings, trunking-secure, trunking-termination, tts-google, turnmegabytes, turnmegabytes-australia, turnmegabytes-brasil, turnmegabytes-germany, turnmegabytes-india, turnmegabytes-ireland, turnmegabytes-japan, turnmegabytes-singapore, turnmegabytes-useast, turnmegabytes-uswest, twilio-interconnect, verify-push, verify-totp, verify-whatsapp-conversations-business-initiated, video-recordings, virtual-agent, voice-insights, voice-insights-client-insights-on-demand-minute, voice-insights-ptsn-insights-on-demand-minute, voice-insights-sip-interface-insights-on-demand-minute, voice-insights-sip-trunking-insights-on-demand-minute, voice-intelligence, voice-intelligence-transcription, voice-intelligence-operators, wireless, wireless-orders, wireless-orders-artwork, wireless-orders-bulk, wireless-orders-esim, wireless-orders-starter, wireless-usage, wireless-usage-commands, wireless-usage-commands-africa, wireless-usage-commands-asia, wireless-usage-commands-centralandsouthamerica, wireless-usage-commands-europe, wireless-usage-commands-home, wireless-usage-commands-northamerica, wireless-usage-commands-oceania, wireless-usage-commands-roaming, wireless-usage-data, wireless-usage-data-africa, wireless-usage-data-asia, wireless-usage-data-centralandsouthamerica, wireless-usage-data-custom-additionalmb, wireless-usage-data-custom-first5mb, wireless-usage-data-domestic-roaming, wireless-usage-data-europe, wireless-usage-data-individual-additionalgb, wireless-usage-data-individual-firstgb, wireless-usage-data-international-roaming-canada, wireless-usage-data-international-roaming-india, wireless-usage-data-international-roaming-mexico, wireless-usage-data-northamerica, wireless-usage-data-oceania, wireless-usage-data-pooled, wireless-usage-data-pooled-downlink, wireless-usage-data-pooled-uplink, wireless-usage-mrc, wireless-usage-mrc-custom, wireless-usage-mrc-individual, wireless-usage-mrc-pooled, wireless-usage-mrc-suspended, wireless-usage-sms, wireless-usage-voice] |
| **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **recurring** | **UsageTriggerEnumRecurring**|  | [optional] [enum: daily, monthly, yearly, alltime] |
| **triggerBy** | **UsageTriggerEnumTriggerField**|  | [optional] [enum: count, usage, price] |

### Return type

[**ApiV2010AccountUsageUsageTrigger**](ApiV2010AccountUsageUsageTrigger.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteUsageTrigger"></a>
# **deleteUsageTrigger**
> deleteUsageTrigger(accountSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401TriggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401TriggerApi apiInstance = new Api20100401TriggerApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete.
    try {
      apiInstance.deleteUsageTrigger(accountSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401TriggerApi#deleteUsageTrigger");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete. | |

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

<a id="fetchUsageTrigger"></a>
# **fetchUsageTrigger**
> ApiV2010AccountUsageUsageTrigger fetchUsageTrigger(accountSid, sid)



Fetch and instance of a usage-trigger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401TriggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401TriggerApi apiInstance = new Api20100401TriggerApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch.
    try {
      ApiV2010AccountUsageUsageTrigger result = apiInstance.fetchUsageTrigger(accountSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401TriggerApi#fetchUsageTrigger");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch. | |

### Return type

[**ApiV2010AccountUsageUsageTrigger**](ApiV2010AccountUsageUsageTrigger.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listUsageTrigger"></a>
# **listUsageTrigger**
> ListUsageTriggerResponse listUsageTrigger(accountSid, recurring, triggerBy, usageCategory, pageSize, page, pageToken)



Retrieve a list of usage-triggers belonging to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401TriggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401TriggerApi apiInstance = new Api20100401TriggerApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to read.
    UsageTriggerEnumRecurring recurring = UsageTriggerEnumRecurring.fromValue("daily"); // UsageTriggerEnumRecurring | The frequency of recurring UsageTriggers to read. Can be: `daily`, `monthly`, or `yearly` to read recurring UsageTriggers. An empty value or a value of `alltime` reads non-recurring UsageTriggers.
    UsageTriggerEnumTriggerField triggerBy = UsageTriggerEnumTriggerField.fromValue("count"); // UsageTriggerEnumTriggerField | The trigger field of the UsageTriggers to read.  Can be: `count`, `usage`, or `price` as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price).
    UsageTriggerEnumUsageCategory usageCategory = UsageTriggerEnumUsageCategory.fromValue("a2p-registration-fees"); // UsageTriggerEnumUsageCategory | The usage category of the UsageTriggers to read. Must be a supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories).
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListUsageTriggerResponse result = apiInstance.listUsageTrigger(accountSid, recurring, triggerBy, usageCategory, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401TriggerApi#listUsageTrigger");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to read. | |
| **recurring** | **UsageTriggerEnumRecurring**| The frequency of recurring UsageTriggers to read. Can be: &#x60;daily&#x60;, &#x60;monthly&#x60;, or &#x60;yearly&#x60; to read recurring UsageTriggers. An empty value or a value of &#x60;alltime&#x60; reads non-recurring UsageTriggers. | [optional] [enum: daily, monthly, yearly, alltime] |
| **triggerBy** | **UsageTriggerEnumTriggerField**| The trigger field of the UsageTriggers to read.  Can be: &#x60;count&#x60;, &#x60;usage&#x60;, or &#x60;price&#x60; as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price). | [optional] [enum: count, usage, price] |
| **usageCategory** | **UsageTriggerEnumUsageCategory**| The usage category of the UsageTriggers to read. Must be a supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories). | [optional] [enum: a2p-registration-fees, agent-conference, amazon-polly, answering-machine-detection, authy-authentications, authy-calls-outbound, authy-monthly-fees, authy-phone-intelligence, authy-phone-verifications, authy-sms-outbound, call-progess-events, calleridlookups, calls, calls-client, calls-globalconference, calls-inbound, calls-inbound-local, calls-inbound-mobile, calls-inbound-tollfree, calls-outbound, calls-pay-verb-transactions, calls-recordings, calls-sip, calls-sip-inbound, calls-sip-outbound, calls-transfers, carrier-lookups, conversations, conversations-api-requests, conversations-conversation-events, conversations-endpoint-connectivity, conversations-events, conversations-participant-events, conversations-participants, cps, flex-usage, fraud-lookups, group-rooms, group-rooms-data-track, group-rooms-encrypted-media-recorded, group-rooms-media-downloaded, group-rooms-media-recorded, group-rooms-media-routed, group-rooms-media-stored, group-rooms-participant-minutes, group-rooms-recorded-minutes, imp-v1-usage, lookups, marketplace, marketplace-algorithmia-named-entity-recognition, marketplace-cadence-transcription, marketplace-cadence-translation, marketplace-capio-speech-to-text, marketplace-convriza-ababa, marketplace-deepgram-phrase-detector, marketplace-digital-segment-business-info, marketplace-facebook-offline-conversions, marketplace-google-speech-to-text, marketplace-ibm-watson-message-insights, marketplace-ibm-watson-message-sentiment, marketplace-ibm-watson-recording-analysis, marketplace-ibm-watson-tone-analyzer, marketplace-icehook-systems-scout, marketplace-infogroup-dataaxle-bizinfo, marketplace-keen-io-contact-center-analytics, marketplace-marchex-cleancall, marketplace-marchex-sentiment-analysis-for-sms, marketplace-marketplace-nextcaller-social-id, marketplace-mobile-commons-opt-out-classifier, marketplace-nexiwave-voicemail-to-text, marketplace-nextcaller-advanced-caller-identification, marketplace-nomorobo-spam-score, marketplace-payfone-tcpa-compliance, marketplace-remeeting-automatic-speech-recognition, marketplace-tcpa-defense-solutions-blacklist-feed, marketplace-telo-opencnam, marketplace-truecnam-true-spam, marketplace-twilio-caller-name-lookup-us, marketplace-twilio-carrier-information-lookup, marketplace-voicebase-pci, marketplace-voicebase-transcription, marketplace-voicebase-transcription-custom-vocabulary, marketplace-whitepages-pro-caller-identification, marketplace-whitepages-pro-phone-intelligence, marketplace-whitepages-pro-phone-reputation, marketplace-wolfarm-spoken-results, marketplace-wolfram-short-answer, marketplace-ytica-contact-center-reporting-analytics, mediastorage, mms, mms-inbound, mms-inbound-longcode, mms-inbound-shortcode, mms-messages-carrierfees, mms-outbound, mms-outbound-longcode, mms-outbound-shortcode, monitor-reads, monitor-storage, monitor-writes, notify, notify-actions-attempts, notify-channels, number-format-lookups, pchat, pchat-users, peer-to-peer-rooms-participant-minutes, pfax, pfax-minutes, pfax-minutes-inbound, pfax-minutes-outbound, pfax-pages, phonenumbers, phonenumbers-cps, phonenumbers-emergency, phonenumbers-local, phonenumbers-mobile, phonenumbers-setups, phonenumbers-tollfree, premiumsupport, proxy, proxy-active-sessions, pstnconnectivity, pv, pv-composition-media-downloaded, pv-composition-media-encrypted, pv-composition-media-stored, pv-composition-minutes, pv-recording-compositions, pv-room-participants, pv-room-participants-au1, pv-room-participants-br1, pv-room-participants-ie1, pv-room-participants-jp1, pv-room-participants-sg1, pv-room-participants-us1, pv-room-participants-us2, pv-rooms, pv-sip-endpoint-registrations, recordings, recordingstorage, rooms-group-bandwidth, rooms-group-minutes, rooms-peer-to-peer-minutes, shortcodes, shortcodes-customerowned, shortcodes-mms-enablement, shortcodes-mps, shortcodes-random, shortcodes-uk, shortcodes-vanity, small-group-rooms, small-group-rooms-data-track, small-group-rooms-participant-minutes, sms, sms-inbound, sms-inbound-longcode, sms-inbound-shortcode, sms-messages-carrierfees, sms-messages-features, sms-messages-features-senderid, sms-outbound, sms-outbound-content-inspection, sms-outbound-longcode, sms-outbound-shortcode, speech-recognition, studio-engagements, sync, sync-actions, sync-endpoint-hours, sync-endpoint-hours-above-daily-cap, taskrouter-tasks, totalprice, transcriptions, trunking-cps, trunking-emergency-calls, trunking-origination, trunking-origination-local, trunking-origination-mobile, trunking-origination-tollfree, trunking-recordings, trunking-secure, trunking-termination, tts-google, turnmegabytes, turnmegabytes-australia, turnmegabytes-brasil, turnmegabytes-germany, turnmegabytes-india, turnmegabytes-ireland, turnmegabytes-japan, turnmegabytes-singapore, turnmegabytes-useast, turnmegabytes-uswest, twilio-interconnect, verify-push, verify-totp, verify-whatsapp-conversations-business-initiated, video-recordings, virtual-agent, voice-insights, voice-insights-client-insights-on-demand-minute, voice-insights-ptsn-insights-on-demand-minute, voice-insights-sip-interface-insights-on-demand-minute, voice-insights-sip-trunking-insights-on-demand-minute, voice-intelligence, voice-intelligence-transcription, voice-intelligence-operators, wireless, wireless-orders, wireless-orders-artwork, wireless-orders-bulk, wireless-orders-esim, wireless-orders-starter, wireless-usage, wireless-usage-commands, wireless-usage-commands-africa, wireless-usage-commands-asia, wireless-usage-commands-centralandsouthamerica, wireless-usage-commands-europe, wireless-usage-commands-home, wireless-usage-commands-northamerica, wireless-usage-commands-oceania, wireless-usage-commands-roaming, wireless-usage-data, wireless-usage-data-africa, wireless-usage-data-asia, wireless-usage-data-centralandsouthamerica, wireless-usage-data-custom-additionalmb, wireless-usage-data-custom-first5mb, wireless-usage-data-domestic-roaming, wireless-usage-data-europe, wireless-usage-data-individual-additionalgb, wireless-usage-data-individual-firstgb, wireless-usage-data-international-roaming-canada, wireless-usage-data-international-roaming-india, wireless-usage-data-international-roaming-mexico, wireless-usage-data-northamerica, wireless-usage-data-oceania, wireless-usage-data-pooled, wireless-usage-data-pooled-downlink, wireless-usage-data-pooled-uplink, wireless-usage-mrc, wireless-usage-mrc-custom, wireless-usage-mrc-individual, wireless-usage-mrc-pooled, wireless-usage-mrc-suspended, wireless-usage-sms, wireless-usage-voice] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListUsageTriggerResponse**](ListUsageTriggerResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateUsageTrigger"></a>
# **updateUsageTrigger**
> ApiV2010AccountUsageUsageTrigger updateUsageTrigger(accountSid, sid, callbackMethod, callbackUrl, friendlyName)



Update an instance of a usage trigger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401TriggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401TriggerApi apiInstance = new Api20100401TriggerApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.
    String callbackMethod = "HEAD"; // String | The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is `POST`.
    URI callbackUrl = new URI(); // URI | The URL we should call using `callback_method` when the trigger fires.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    try {
      ApiV2010AccountUsageUsageTrigger result = apiInstance.updateUsageTrigger(accountSid, sid, callbackMethod, callbackUrl, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401TriggerApi#updateUsageTrigger");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the UsageTrigger resource to update. | |
| **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **callbackUrl** | **URI**| The URL we should call using &#x60;callback_method&#x60; when the trigger fires. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |

### Return type

[**ApiV2010AccountUsageUsageTrigger**](ApiV2010AccountUsageUsageTrigger.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

