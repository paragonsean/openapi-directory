

# InsightsV1CallMetric


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique SID identifier of the Account. |  [optional] |
|**callSid** | **String** | The unique SID identifier of the Call. |  [optional] |
|**carrierEdge** | **Object** | Contains metrics and properties for the Twilio media gateway of a PSTN call. |  [optional] |
|**clientEdge** | **Object** | Contains metrics and properties for the Twilio media gateway of a Client call. |  [optional] |
|**direction** | **MetricEnumStreamDirection** |  |  [optional] |
|**edge** | **MetricEnumTwilioEdge** |  |  [optional] |
|**sdkEdge** | **Object** | Contains metrics and properties for the SDK sensor library for Client calls. |  [optional] |
|**sipEdge** | **Object** | Contains metrics and properties for the Twilio media gateway of a SIP Interface or Trunking call. |  [optional] |
|**timestamp** | **String** | Timestamp of metric sample. Samples are taken every 10 seconds and contain the metrics for the previous 10 seconds. |  [optional] |



