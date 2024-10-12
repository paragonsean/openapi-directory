# AlerterSystemApi.TransportClickSendJsonldGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  | [optional] 
**id** | **String** |  | [optional] [readonly] 
**type** | **String** |  | [optional] [readonly] 
**clickSendApiKey** | **String** | The API key for the ClickSend service. Stored in encrypted format. | 
**clickSendApiUsername** | **String** | The API username for the ClickSend service. | 
**clickSendFrom** | **String** | The from value for the ClickSend service. | [optional] 
**clickSendFromEmail** | **String** | The from email value where replies must be emailed for the ClickSend service. | [optional] 
**clickSendListId** | **String** | The recipient list ID value for the ClickSend service. | [optional] 
**clickSendSource** | **String** | The source method of sending value for the ClickSend service. | [optional] 
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**transportName** | **String** | The name of the transport. | 


