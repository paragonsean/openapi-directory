# AlerterSystemApi.TransportOvhCloudGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**ovhCloudApplicationKey** | **String** | The application key for the OVHcloud service. | 
**ovhCloudApplicationSecret** | **String** | The application secret for the OVHcloud service. Stored in encrypted format. | 
**ovhCloudConsumerKey** | **String** | The consumer key for the OVHcloud service. | 
**ovhCloudSender** | **String** | The optional sender for the OVHcloud service. | [optional] 
**ovhCloudServiceName** | **String** | The service name for the OVHcloud service. | 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**transportName** | **String** | The name of the transport. | 


