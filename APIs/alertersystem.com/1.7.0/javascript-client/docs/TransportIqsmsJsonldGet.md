# AlerterSystemApi.TransportIqsmsJsonldGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  | [optional] 
**id** | **String** |  | [optional] [readonly] 
**type** | **String** |  | [optional] [readonly] 
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**iqsmsFrom** | **String** | The sender value for the Iqsms service. | 
**iqsmsLogin** | **String** | The login for the Iqsms service. | 
**iqsmsPassword** | **String** | The password for the Iqsms service. Stored in encrypted format. | 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**transportName** | **String** | The name of the transport. | 


