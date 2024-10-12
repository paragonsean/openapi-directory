

# TransportClickSendPatch

The TransportClickSend resource is a collection of transports that carry dispatched alerts to the external ClickSend service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clickSendApiKey** | **String** | The API key for the ClickSend service. Stored in encrypted format. |  |
|**clickSendApiUsername** | **String** | The API username for the ClickSend service. |  |
|**clickSendFrom** | **String** | The from value for the ClickSend service. |  [optional] |
|**clickSendFromEmail** | **String** | The from email value where replies must be emailed for the ClickSend service. |  [optional] |
|**clickSendListId** | **String** | The recipient list ID value for the ClickSend service. |  [optional] |
|**clickSendSource** | **String** | The source method of sending value for the ClickSend service. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |



