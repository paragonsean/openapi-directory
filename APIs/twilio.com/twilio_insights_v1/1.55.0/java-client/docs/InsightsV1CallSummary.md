

# InsightsV1CallSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique SID identifier of the Account. |  [optional] |
|**annotation** | **Object** | Programmatically labeled annotations for the Call. Developers can update the Call Summary records with Annotation during or after a Call. Annotations can be updated as long as the Call Summary record is addressable via the API. |  [optional] |
|**answeredBy** | **SummaryEnumAnsweredBy** |  |  [optional] |
|**attributes** | **Object** | Attributes capturing call-flow-specific details. |  [optional] |
|**callSid** | **String** | The unique SID identifier of the Call. |  [optional] |
|**callState** | **SummaryEnumCallState** |  |  [optional] |
|**callType** | **SummaryEnumCallType** |  |  [optional] |
|**carrierEdge** | **Object** | Contains metrics and properties for the Twilio media gateway of a PSTN call. |  [optional] |
|**clientEdge** | **Object** | Contains metrics and properties for the Twilio media gateway of a Client call. |  [optional] |
|**connectDuration** | **Integer** | Duration between when the call was answered and when it ended |  [optional] |
|**createdTime** | **OffsetDateTime** | The time at which the Call was created, given in ISO 8601 format. Can be different from &#x60;start_time&#x60; in the event of queueing due to CPS |  [optional] |
|**duration** | **Integer** | Duration between when the call was initiated and the call was ended |  [optional] |
|**endTime** | **OffsetDateTime** | The time at which the Call was ended, given in ISO 8601 format. |  [optional] |
|**from** | **Object** | The calling party. |  [optional] |
|**processingState** | **SummaryEnumProcessingState** |  |  [optional] |
|**properties** | **Object** | Contains edge-agnostic call-level details. |  [optional] |
|**sdkEdge** | **Object** | Contains metrics and properties for the SDK sensor library for Client calls. |  [optional] |
|**sipEdge** | **Object** | Contains metrics and properties for the Twilio media gateway of a SIP Interface or Trunking call. |  [optional] |
|**startTime** | **OffsetDateTime** | The time at which the Call was started, given in ISO 8601 format. |  [optional] |
|**tags** | **List&lt;String&gt;** | Tags applied to calls by Voice Insights analysis indicating a condition that could result in subjective degradation of the call quality. |  [optional] |
|**to** | **Object** | The called party. |  [optional] |
|**trust** | **Object** | Contains trusted communications details including Branded Call and verified caller ID. |  [optional] |
|**url** | **URI** | The URL of this resource. |  [optional] |



