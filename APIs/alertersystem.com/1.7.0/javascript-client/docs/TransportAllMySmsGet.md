# AlerterSystemApi.TransportAllMySmsGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allMySmsApiKey** | **String** | The API key for the Allmysms service. Stored in encrypted format. | 
**allMySmsFrom** | **String** | The sender value (default 36180) for the Allmysms service. | [optional] 
**allMySmsLogin** | **String** | The login credential for the Allmysms service. | 
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**transportName** | **String** | The name of the transport. | 


