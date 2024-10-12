

# InsightsV1CallEvent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique SID identifier of the Account. |  [optional] |
|**callSid** | **String** | The unique SID identifier of the Call. |  [optional] |
|**carrierEdge** | **Object** | Represents the connection between Twilio and our immediate carrier partners. The events here describe the call lifecycle as reported by Twilio&#39;s carrier media gateways. |  [optional] |
|**clientEdge** | **Object** | Represents the Twilio media gateway for Client calls. The events here describe the call lifecycle as reported by Twilio&#39;s Voice SDK media gateways. |  [optional] |
|**edge** | **EventEnumTwilioEdge** |  |  [optional] |
|**group** | **String** | Event group. |  [optional] |
|**level** | **EventEnumLevel** |  |  [optional] |
|**name** | **String** | Event name. |  [optional] |
|**sdkEdge** | **Object** | Represents the Voice SDK running locally in the browser or in the Android/iOS application. The events here are emitted by the Voice SDK in response to certain call progress events, network changes, or call quality conditions. |  [optional] |
|**sipEdge** | **Object** | Represents the Twilio media gateway for SIP interface and SIP trunking calls. The events here describe the call lifecycle as reported by Twilio&#39;s public media gateways. |  [optional] |
|**timestamp** | **String** | Event time. |  [optional] |



