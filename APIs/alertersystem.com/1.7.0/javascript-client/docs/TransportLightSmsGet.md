# AlerterSystemApi.TransportLightSmsGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**lightSmsLogin** | **String** | The login for the LightSMS service. | 
**lightSmsPhone** | **String** | The sender phone number for the LightSMS service. | 
**lightSmsToken** | **String** | The token for the LightSMS service. Stored in encrypted format. | 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**transportName** | **String** | The name of the transport. | 


