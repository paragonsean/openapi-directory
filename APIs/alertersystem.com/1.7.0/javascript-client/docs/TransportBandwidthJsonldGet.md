# AlerterSystemApi.TransportBandwidthJsonldGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  | [optional] 
**id** | **String** |  | [optional] [readonly] 
**type** | **String** |  | [optional] [readonly] 
**bandwidthAccountId** | **String** | The account ID value for the Bandwidth service. | 
**bandwidthApplicationId** | **String** | The application ID value for the Bandwidth service. | 
**bandwidthFrom** | **String** | The from value for the Bandwidth service. | 
**bandwidthPassword** | **String** | The password for the Bandwidth service. Stored in encrypted format. | 
**bandwidthUsername** | **String** | The username for the Bandwidth service. | 
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**transportName** | **String** | The name of the transport. | 


