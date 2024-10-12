# AlerterSystemApi.TransportSms77Get

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**sms77ApiKey** | **String** | The API key for the Sms77 service. Stored in encrypted format. | 
**sms77From** | **String** | The optional sender for the Sms77 service. | [optional] 
**transportName** | **String** | The name of the transport. | 


