# TwilioInsights.InsightsV1CallSummariesApi

All URIs are relative to *https://insights.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listCallSummaries**](InsightsV1CallSummariesApi.md#listCallSummaries) | **GET** /v1/Voice/Summaries | 



## listCallSummaries

> ListCallSummariesResponse listCallSummaries(opts)



Get a list of Call Summaries.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1CallSummariesApi();
let opts = {
  'from': "from_example", // String | A calling party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
  'to': "to_example", // String | A called party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
  'fromCarrier': "fromCarrier_example", // String | An origination carrier.
  'toCarrier': "toCarrier_example", // String | A destination carrier.
  'fromCountryCode': "fromCountryCode_example", // String | A source country code based on phone number in From.
  'toCountryCode': "toCountryCode_example", // String | A destination country code. Based on phone number in To.
  'branded': true, // Boolean | A boolean flag indicating whether or not the calls were branded using Twilio Branded Calls.
  'verifiedCaller': true, // Boolean | A boolean flag indicating whether or not the caller was verified using SHAKEN/STIR.
  'hasTag': true, // Boolean | A boolean flag indicating the presence of one or more [Voice Insights Call Tags](https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-tags).
  'startTime': "startTime_example", // String | A Start time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or datetime-ISO. Defaults to 4h.
  'endTime': "endTime_example", // String | An End Time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or datetime-ISO. Defaults to 0m.
  'callType': "callType_example", // String | A Call Type of the calls. One of `carrier`, `sip`, `trunking` or `client`.
  'callState': "callState_example", // String | A Call State of the calls. One of `ringing`, `completed`, `busy`, `fail`, `noanswer`, `canceled`, `answered`, `undialed`.
  'direction': "direction_example", // String | A Direction of the calls. One of `outbound_api`, `outbound_dial`, `inbound`, `trunking_originating`, `trunking_terminating`.
  'processingState': "processingState_example", // CallSummariesEnumProcessingStateRequest | A Processing State of the Call Summaries. One of `completed`, `partial` or `all`.
  'sortBy': "sortBy_example", // CallSummariesEnumSortBy | A Sort By criterion for the returned list of Call Summaries. One of `start_time` or `end_time`.
  'subaccount': "subaccount_example", // String | A unique SID identifier of a Subaccount.
  'abnormalSession': true, // Boolean | A boolean flag indicating an abnormal session where the last SIP response was not 200 OK.
  'answeredBy': "answeredBy_example", // CallSummariesEnumAnsweredBy | An Answered By value for the calls based on `Answering Machine Detection (AMD)`. One of `unknown`, `machine_start`, `machine_end_beep`, `machine_end_silence`, `machine_end_other`, `human` or `fax`.
  'answeredByAnnotation': "answeredByAnnotation_example", // String | Either machine or human.
  'connectivityIssueAnnotation': "connectivityIssueAnnotation_example", // String | A Connectivity Issue with the calls. One of `no_connectivity_issue`, `invalid_number`, `caller_id`, `dropped_call`, or `number_reachability`.
  'qualityIssueAnnotation': "qualityIssueAnnotation_example", // String | A subjective Quality Issue with the calls. One of `no_quality_issue`, `low_volume`, `choppy_robotic`, `echo`, `dtmf`, `latency`, `owa`, `static_noise`.
  'spamAnnotation': true, // Boolean | A boolean flag indicating spam calls.
  'callScoreAnnotation': "callScoreAnnotation_example", // String | A Call Score of the calls. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for the rated call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad].
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listCallSummaries(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from** | **String**| A calling party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name. | [optional] 
 **to** | **String**| A called party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name. | [optional] 
 **fromCarrier** | **String**| An origination carrier. | [optional] 
 **toCarrier** | **String**| A destination carrier. | [optional] 
 **fromCountryCode** | **String**| A source country code based on phone number in From. | [optional] 
 **toCountryCode** | **String**| A destination country code. Based on phone number in To. | [optional] 
 **branded** | **Boolean**| A boolean flag indicating whether or not the calls were branded using Twilio Branded Calls. | [optional] 
 **verifiedCaller** | **Boolean**| A boolean flag indicating whether or not the caller was verified using SHAKEN/STIR. | [optional] 
 **hasTag** | **Boolean**| A boolean flag indicating the presence of one or more [Voice Insights Call Tags](https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-tags). | [optional] 
 **startTime** | **String**| A Start time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or datetime-ISO. Defaults to 4h. | [optional] 
 **endTime** | **String**| An End Time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or datetime-ISO. Defaults to 0m. | [optional] 
 **callType** | **String**| A Call Type of the calls. One of &#x60;carrier&#x60;, &#x60;sip&#x60;, &#x60;trunking&#x60; or &#x60;client&#x60;. | [optional] 
 **callState** | **String**| A Call State of the calls. One of &#x60;ringing&#x60;, &#x60;completed&#x60;, &#x60;busy&#x60;, &#x60;fail&#x60;, &#x60;noanswer&#x60;, &#x60;canceled&#x60;, &#x60;answered&#x60;, &#x60;undialed&#x60;. | [optional] 
 **direction** | **String**| A Direction of the calls. One of &#x60;outbound_api&#x60;, &#x60;outbound_dial&#x60;, &#x60;inbound&#x60;, &#x60;trunking_originating&#x60;, &#x60;trunking_terminating&#x60;. | [optional] 
 **processingState** | **CallSummariesEnumProcessingStateRequest**| A Processing State of the Call Summaries. One of &#x60;completed&#x60;, &#x60;partial&#x60; or &#x60;all&#x60;. | [optional] 
 **sortBy** | **CallSummariesEnumSortBy**| A Sort By criterion for the returned list of Call Summaries. One of &#x60;start_time&#x60; or &#x60;end_time&#x60;. | [optional] 
 **subaccount** | **String**| A unique SID identifier of a Subaccount. | [optional] 
 **abnormalSession** | **Boolean**| A boolean flag indicating an abnormal session where the last SIP response was not 200 OK. | [optional] 
 **answeredBy** | **CallSummariesEnumAnsweredBy**| An Answered By value for the calls based on &#x60;Answering Machine Detection (AMD)&#x60;. One of &#x60;unknown&#x60;, &#x60;machine_start&#x60;, &#x60;machine_end_beep&#x60;, &#x60;machine_end_silence&#x60;, &#x60;machine_end_other&#x60;, &#x60;human&#x60; or &#x60;fax&#x60;. | [optional] 
 **answeredByAnnotation** | **String**| Either machine or human. | [optional] 
 **connectivityIssueAnnotation** | **String**| A Connectivity Issue with the calls. One of &#x60;no_connectivity_issue&#x60;, &#x60;invalid_number&#x60;, &#x60;caller_id&#x60;, &#x60;dropped_call&#x60;, or &#x60;number_reachability&#x60;. | [optional] 
 **qualityIssueAnnotation** | **String**| A subjective Quality Issue with the calls. One of &#x60;no_quality_issue&#x60;, &#x60;low_volume&#x60;, &#x60;choppy_robotic&#x60;, &#x60;echo&#x60;, &#x60;dtmf&#x60;, &#x60;latency&#x60;, &#x60;owa&#x60;, &#x60;static_noise&#x60;. | [optional] 
 **spamAnnotation** | **Boolean**| A boolean flag indicating spam calls. | [optional] 
 **callScoreAnnotation** | **String**| A Call Score of the calls. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for the rated call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad]. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListCallSummariesResponse**](ListCallSummariesResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

