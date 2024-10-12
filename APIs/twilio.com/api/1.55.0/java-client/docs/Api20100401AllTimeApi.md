# Api20100401AllTimeApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listUsageRecordAllTime**](Api20100401AllTimeApi.md#listUsageRecordAllTime) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Records/AllTime.json |  |


<a id="listUsageRecordAllTime"></a>
# **listUsageRecordAllTime**
> ListUsageRecordAllTimeResponse listUsageRecordAllTime(accountSid, category, startDate, endDate, includeSubaccounts, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AllTimeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AllTimeApi apiInstance = new Api20100401AllTimeApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
    UsageRecordAllTimeEnumCategory category = UsageRecordAllTimeEnumCategory.fromValue("a2p-registration-fees"); // UsageRecordAllTimeEnumCategory | The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
    LocalDate startDate = LocalDate.now(); // LocalDate | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date.
    LocalDate endDate = LocalDate.now(); // LocalDate | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date.
    Boolean includeSubaccounts = true; // Boolean | Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListUsageRecordAllTimeResponse result = apiInstance.listUsageRecordAllTime(accountSid, category, startDate, endDate, includeSubaccounts, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AllTimeApi#listUsageRecordAllTime");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read. | |
| **category** | **UsageRecordAllTimeEnumCategory**| The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. | [optional] [enum: a2p-registration-fees, agent-conference, amazon-polly, answering-machine-detection, authy-authentications, authy-calls-outbound, authy-monthly-fees, authy-phone-intelligence, authy-phone-verifications, authy-sms-outbound, call-progess-events, calleridlookups, calls, calls-client, calls-globalconference, calls-inbound, calls-inbound-local, calls-inbound-mobile, calls-inbound-tollfree, calls-outbound, calls-pay-verb-transactions, calls-recordings, calls-sip, calls-sip-inbound, calls-sip-outbound, calls-transfers, carrier-lookups, conversations, conversations-api-requests, conversations-conversation-events, conversations-endpoint-connectivity, conversations-events, conversations-participant-events, conversations-participants, cps, flex-usage, fraud-lookups, group-rooms, group-rooms-data-track, group-rooms-encrypted-media-recorded, group-rooms-media-downloaded, group-rooms-media-recorded, group-rooms-media-routed, group-rooms-media-stored, group-rooms-participant-minutes, group-rooms-recorded-minutes, imp-v1-usage, lookups, marketplace, marketplace-algorithmia-named-entity-recognition, marketplace-cadence-transcription, marketplace-cadence-translation, marketplace-capio-speech-to-text, marketplace-convriza-ababa, marketplace-deepgram-phrase-detector, marketplace-digital-segment-business-info, marketplace-facebook-offline-conversions, marketplace-google-speech-to-text, marketplace-ibm-watson-message-insights, marketplace-ibm-watson-message-sentiment, marketplace-ibm-watson-recording-analysis, marketplace-ibm-watson-tone-analyzer, marketplace-icehook-systems-scout, marketplace-infogroup-dataaxle-bizinfo, marketplace-keen-io-contact-center-analytics, marketplace-marchex-cleancall, marketplace-marchex-sentiment-analysis-for-sms, marketplace-marketplace-nextcaller-social-id, marketplace-mobile-commons-opt-out-classifier, marketplace-nexiwave-voicemail-to-text, marketplace-nextcaller-advanced-caller-identification, marketplace-nomorobo-spam-score, marketplace-payfone-tcpa-compliance, marketplace-remeeting-automatic-speech-recognition, marketplace-tcpa-defense-solutions-blacklist-feed, marketplace-telo-opencnam, marketplace-truecnam-true-spam, marketplace-twilio-caller-name-lookup-us, marketplace-twilio-carrier-information-lookup, marketplace-voicebase-pci, marketplace-voicebase-transcription, marketplace-voicebase-transcription-custom-vocabulary, marketplace-whitepages-pro-caller-identification, marketplace-whitepages-pro-phone-intelligence, marketplace-whitepages-pro-phone-reputation, marketplace-wolfarm-spoken-results, marketplace-wolfram-short-answer, marketplace-ytica-contact-center-reporting-analytics, mediastorage, mms, mms-inbound, mms-inbound-longcode, mms-inbound-shortcode, mms-messages-carrierfees, mms-outbound, mms-outbound-longcode, mms-outbound-shortcode, monitor-reads, monitor-storage, monitor-writes, notify, notify-actions-attempts, notify-channels, number-format-lookups, pchat, pchat-users, peer-to-peer-rooms-participant-minutes, pfax, pfax-minutes, pfax-minutes-inbound, pfax-minutes-outbound, pfax-pages, phonenumbers, phonenumbers-cps, phonenumbers-emergency, phonenumbers-local, phonenumbers-mobile, phonenumbers-setups, phonenumbers-tollfree, premiumsupport, proxy, proxy-active-sessions, pstnconnectivity, pv, pv-composition-media-downloaded, pv-composition-media-encrypted, pv-composition-media-stored, pv-composition-minutes, pv-recording-compositions, pv-room-participants, pv-room-participants-au1, pv-room-participants-br1, pv-room-participants-ie1, pv-room-participants-jp1, pv-room-participants-sg1, pv-room-participants-us1, pv-room-participants-us2, pv-rooms, pv-sip-endpoint-registrations, recordings, recordingstorage, rooms-group-bandwidth, rooms-group-minutes, rooms-peer-to-peer-minutes, shortcodes, shortcodes-customerowned, shortcodes-mms-enablement, shortcodes-mps, shortcodes-random, shortcodes-uk, shortcodes-vanity, small-group-rooms, small-group-rooms-data-track, small-group-rooms-participant-minutes, sms, sms-inbound, sms-inbound-longcode, sms-inbound-shortcode, sms-messages-carrierfees, sms-messages-features, sms-messages-features-senderid, sms-outbound, sms-outbound-content-inspection, sms-outbound-longcode, sms-outbound-shortcode, speech-recognition, studio-engagements, sync, sync-actions, sync-endpoint-hours, sync-endpoint-hours-above-daily-cap, taskrouter-tasks, totalprice, transcriptions, trunking-cps, trunking-emergency-calls, trunking-origination, trunking-origination-local, trunking-origination-mobile, trunking-origination-tollfree, trunking-recordings, trunking-secure, trunking-termination, tts-google, turnmegabytes, turnmegabytes-australia, turnmegabytes-brasil, turnmegabytes-germany, turnmegabytes-india, turnmegabytes-ireland, turnmegabytes-japan, turnmegabytes-singapore, turnmegabytes-useast, turnmegabytes-uswest, twilio-interconnect, verify-push, verify-totp, verify-whatsapp-conversations-business-initiated, video-recordings, virtual-agent, voice-insights, voice-insights-client-insights-on-demand-minute, voice-insights-ptsn-insights-on-demand-minute, voice-insights-sip-interface-insights-on-demand-minute, voice-insights-sip-trunking-insights-on-demand-minute, voice-intelligence, voice-intelligence-transcription, voice-intelligence-operators, wireless, wireless-orders, wireless-orders-artwork, wireless-orders-bulk, wireless-orders-esim, wireless-orders-starter, wireless-usage, wireless-usage-commands, wireless-usage-commands-africa, wireless-usage-commands-asia, wireless-usage-commands-centralandsouthamerica, wireless-usage-commands-europe, wireless-usage-commands-home, wireless-usage-commands-northamerica, wireless-usage-commands-oceania, wireless-usage-commands-roaming, wireless-usage-data, wireless-usage-data-africa, wireless-usage-data-asia, wireless-usage-data-centralandsouthamerica, wireless-usage-data-custom-additionalmb, wireless-usage-data-custom-first5mb, wireless-usage-data-domestic-roaming, wireless-usage-data-europe, wireless-usage-data-individual-additionalgb, wireless-usage-data-individual-firstgb, wireless-usage-data-international-roaming-canada, wireless-usage-data-international-roaming-india, wireless-usage-data-international-roaming-mexico, wireless-usage-data-northamerica, wireless-usage-data-oceania, wireless-usage-data-pooled, wireless-usage-data-pooled-downlink, wireless-usage-data-pooled-uplink, wireless-usage-mrc, wireless-usage-mrc-custom, wireless-usage-mrc-individual, wireless-usage-mrc-pooled, wireless-usage-mrc-suspended, wireless-usage-sms, wireless-usage-voice] |
| **startDate** | **LocalDate**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. You can also specify offsets from the current date, such as: &#x60;-30days&#x60;, which will set the start date to be 30 days before the current date. | [optional] |
| **endDate** | **LocalDate**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.  You can also specify offsets from the current date, such as: &#x60;+30days&#x60;, which will set the end date to 30 days from the current date. | [optional] |
| **includeSubaccounts** | **Boolean**| Whether to include usage from the master account and all its subaccounts. Can be: &#x60;true&#x60; (the default) to include usage from the master account and all subaccounts or &#x60;false&#x60; to retrieve usage from only the specified account. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListUsageRecordAllTimeResponse**](ListUsageRecordAllTimeResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

