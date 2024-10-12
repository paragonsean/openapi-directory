# AlerterSystemApi.MonitorStatusLogGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] [readonly] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**monitor** | **String** | The monitor that is related to this resource instance. | [optional] 
**monitorStatusCode** | **String** | The status of the monitor. | [optional] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | [optional] 
**ping** | **String** | The ping that triggered this resource instance. | [optional] 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 


