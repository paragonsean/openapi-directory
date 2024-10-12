# AlerterSystemApi.TransportPagerDutyGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**pagerDutyApiToken** | **String** | The API token for the Pager Duty service. Stored in encrypted format. | 
**pagerDutyDedupKey** | **String** | The dedup key for the Pager Duty service. | [optional] 
**pagerDutyEventAction** | **String** | The event action for the Pager Duty service. | 
**pagerDutyPayloadClass** | **String** | The payload class for the Pager Duty service. | [optional] 
**pagerDutyPayloadComponent** | **String** | The payload component for the Pager Duty service. | [optional] 
**pagerDutyPayloadGroup** | **String** | The payload group for the Pager Duty service. | [optional] 
**pagerDutyPayloadSeverity** | **String** | The payload severity for the Pager Duty service. | [optional] 
**pagerDutyPayloadSource** | **String** | The payload source for the Pager Duty service. | [optional] 
**pagerDutyRoutingKey** | **String** | The routing key for the Pager Duty service. | 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**transportName** | **String** | The name of the transport. | 


