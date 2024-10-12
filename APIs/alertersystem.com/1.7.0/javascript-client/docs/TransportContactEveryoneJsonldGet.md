# AlerterSystemApi.TransportContactEveryoneJsonldGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  | [optional] 
**id** | **String** |  | [optional] [readonly] 
**type** | **String** |  | [optional] [readonly] 
**contactEveryoneCategory** | **String** | The label of the category that will be displayed in the external service event logs of the ContactEveryone service. | [optional] 
**contactEveryoneDiffusionName** | **String** | The label of the diffusion that will be displayed in the external service event logs of the ContactEveryone service. | [optional] 
**contactEveryoneToken** | **String** | The token for the Contact Everyone service. Stored in encrypted format. | 
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**transportName** | **String** | The name of the transport. | 


