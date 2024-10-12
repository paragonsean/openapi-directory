# InsightsV1CallSummariesApi

All URIs are relative to *https://insights.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listCallSummaries**](InsightsV1CallSummariesApi.md#listCallSummaries) | **GET** /v1/Voice/Summaries |  |


<a id="listCallSummaries"></a>
# **listCallSummaries**
> ListCallSummariesResponse listCallSummaries(from, to, fromCarrier, toCarrier, fromCountryCode, toCountryCode, branded, verifiedCaller, hasTag, startTime, endTime, callType, callState, direction, processingState, sortBy, subaccount, abnormalSession, answeredBy, answeredByAnnotation, connectivityIssueAnnotation, qualityIssueAnnotation, spamAnnotation, callScoreAnnotation, pageSize, page, pageToken)



Get a list of Call Summaries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1CallSummariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1CallSummariesApi apiInstance = new InsightsV1CallSummariesApi(defaultClient);
    String from = "from_example"; // String | A calling party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
    String to = "to_example"; // String | A called party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name.
    String fromCarrier = "fromCarrier_example"; // String | An origination carrier.
    String toCarrier = "toCarrier_example"; // String | A destination carrier.
    String fromCountryCode = "fromCountryCode_example"; // String | A source country code based on phone number in From.
    String toCountryCode = "toCountryCode_example"; // String | A destination country code. Based on phone number in To.
    Boolean branded = true; // Boolean | A boolean flag indicating whether or not the calls were branded using Twilio Branded Calls.
    Boolean verifiedCaller = true; // Boolean | A boolean flag indicating whether or not the caller was verified using SHAKEN/STIR.
    Boolean hasTag = true; // Boolean | A boolean flag indicating the presence of one or more [Voice Insights Call Tags](https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-tags).
    String startTime = "startTime_example"; // String | A Start time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or datetime-ISO. Defaults to 4h.
    String endTime = "endTime_example"; // String | An End Time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or datetime-ISO. Defaults to 0m.
    String callType = "callType_example"; // String | A Call Type of the calls. One of `carrier`, `sip`, `trunking` or `client`.
    String callState = "callState_example"; // String | A Call State of the calls. One of `ringing`, `completed`, `busy`, `fail`, `noanswer`, `canceled`, `answered`, `undialed`.
    String direction = "direction_example"; // String | A Direction of the calls. One of `outbound_api`, `outbound_dial`, `inbound`, `trunking_originating`, `trunking_terminating`.
    CallSummariesEnumProcessingStateRequest processingState = CallSummariesEnumProcessingStateRequest.fromValue("completed"); // CallSummariesEnumProcessingStateRequest | A Processing State of the Call Summaries. One of `completed`, `partial` or `all`.
    CallSummariesEnumSortBy sortBy = CallSummariesEnumSortBy.fromValue("start_time"); // CallSummariesEnumSortBy | A Sort By criterion for the returned list of Call Summaries. One of `start_time` or `end_time`.
    String subaccount = "subaccount_example"; // String | A unique SID identifier of a Subaccount.
    Boolean abnormalSession = true; // Boolean | A boolean flag indicating an abnormal session where the last SIP response was not 200 OK.
    CallSummariesEnumAnsweredBy answeredBy = CallSummariesEnumAnsweredBy.fromValue("unknown"); // CallSummariesEnumAnsweredBy | An Answered By value for the calls based on `Answering Machine Detection (AMD)`. One of `unknown`, `machine_start`, `machine_end_beep`, `machine_end_silence`, `machine_end_other`, `human` or `fax`.
    String answeredByAnnotation = "answeredByAnnotation_example"; // String | Either machine or human.
    String connectivityIssueAnnotation = "connectivityIssueAnnotation_example"; // String | A Connectivity Issue with the calls. One of `no_connectivity_issue`, `invalid_number`, `caller_id`, `dropped_call`, or `number_reachability`.
    String qualityIssueAnnotation = "qualityIssueAnnotation_example"; // String | A subjective Quality Issue with the calls. One of `no_quality_issue`, `low_volume`, `choppy_robotic`, `echo`, `dtmf`, `latency`, `owa`, `static_noise`.
    Boolean spamAnnotation = true; // Boolean | A boolean flag indicating spam calls.
    String callScoreAnnotation = "callScoreAnnotation_example"; // String | A Call Score of the calls. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for the rated call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad].
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCallSummariesResponse result = apiInstance.listCallSummaries(from, to, fromCarrier, toCarrier, fromCountryCode, toCountryCode, branded, verifiedCaller, hasTag, startTime, endTime, callType, callState, direction, processingState, sortBy, subaccount, abnormalSession, answeredBy, answeredByAnnotation, connectivityIssueAnnotation, qualityIssueAnnotation, spamAnnotation, callScoreAnnotation, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1CallSummariesApi#listCallSummaries");
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
| **from** | **String**| A calling party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name. | [optional] |
| **to** | **String**| A called party. Could be an E.164 number, a SIP URI, or a Twilio Client registered name. | [optional] |
| **fromCarrier** | **String**| An origination carrier. | [optional] |
| **toCarrier** | **String**| A destination carrier. | [optional] |
| **fromCountryCode** | **String**| A source country code based on phone number in From. | [optional] |
| **toCountryCode** | **String**| A destination country code. Based on phone number in To. | [optional] |
| **branded** | **Boolean**| A boolean flag indicating whether or not the calls were branded using Twilio Branded Calls. | [optional] |
| **verifiedCaller** | **Boolean**| A boolean flag indicating whether or not the caller was verified using SHAKEN/STIR. | [optional] |
| **hasTag** | **Boolean**| A boolean flag indicating the presence of one or more [Voice Insights Call Tags](https://www.twilio.com/docs/voice/voice-insights/api/call/details-call-tags). | [optional] |
| **startTime** | **String**| A Start time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or datetime-ISO. Defaults to 4h. | [optional] |
| **endTime** | **String**| An End Time of the calls. xm (x minutes), xh (x hours), xd (x days), 1w, 30m, 3d, 4w or datetime-ISO. Defaults to 0m. | [optional] |
| **callType** | **String**| A Call Type of the calls. One of &#x60;carrier&#x60;, &#x60;sip&#x60;, &#x60;trunking&#x60; or &#x60;client&#x60;. | [optional] |
| **callState** | **String**| A Call State of the calls. One of &#x60;ringing&#x60;, &#x60;completed&#x60;, &#x60;busy&#x60;, &#x60;fail&#x60;, &#x60;noanswer&#x60;, &#x60;canceled&#x60;, &#x60;answered&#x60;, &#x60;undialed&#x60;. | [optional] |
| **direction** | **String**| A Direction of the calls. One of &#x60;outbound_api&#x60;, &#x60;outbound_dial&#x60;, &#x60;inbound&#x60;, &#x60;trunking_originating&#x60;, &#x60;trunking_terminating&#x60;. | [optional] |
| **processingState** | **CallSummariesEnumProcessingStateRequest**| A Processing State of the Call Summaries. One of &#x60;completed&#x60;, &#x60;partial&#x60; or &#x60;all&#x60;. | [optional] [enum: completed, started, partial, all] |
| **sortBy** | **CallSummariesEnumSortBy**| A Sort By criterion for the returned list of Call Summaries. One of &#x60;start_time&#x60; or &#x60;end_time&#x60;. | [optional] [enum: start_time, end_time] |
| **subaccount** | **String**| A unique SID identifier of a Subaccount. | [optional] |
| **abnormalSession** | **Boolean**| A boolean flag indicating an abnormal session where the last SIP response was not 200 OK. | [optional] |
| **answeredBy** | **CallSummariesEnumAnsweredBy**| An Answered By value for the calls based on &#x60;Answering Machine Detection (AMD)&#x60;. One of &#x60;unknown&#x60;, &#x60;machine_start&#x60;, &#x60;machine_end_beep&#x60;, &#x60;machine_end_silence&#x60;, &#x60;machine_end_other&#x60;, &#x60;human&#x60; or &#x60;fax&#x60;. | [optional] [enum: unknown, machine_start, machine_end_beep, machine_end_silence, machine_end_other, human, fax] |
| **answeredByAnnotation** | **String**| Either machine or human. | [optional] |
| **connectivityIssueAnnotation** | **String**| A Connectivity Issue with the calls. One of &#x60;no_connectivity_issue&#x60;, &#x60;invalid_number&#x60;, &#x60;caller_id&#x60;, &#x60;dropped_call&#x60;, or &#x60;number_reachability&#x60;. | [optional] |
| **qualityIssueAnnotation** | **String**| A subjective Quality Issue with the calls. One of &#x60;no_quality_issue&#x60;, &#x60;low_volume&#x60;, &#x60;choppy_robotic&#x60;, &#x60;echo&#x60;, &#x60;dtmf&#x60;, &#x60;latency&#x60;, &#x60;owa&#x60;, &#x60;static_noise&#x60;. | [optional] |
| **spamAnnotation** | **Boolean**| A boolean flag indicating spam calls. | [optional] |
| **callScoreAnnotation** | **String**| A Call Score of the calls. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for the rated call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad]. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListCallSummariesResponse**](ListCallSummariesResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

