

# TransportPagerDutyPut

The TransportPagerDuty resource is a collection of transports that carry dispatched alerts to the external Pager Duty service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**pagerDutyApiToken** | **String** | The API token for the Pager Duty service. Stored in encrypted format. |  |
|**pagerDutyDedupKey** | **String** | The dedup key for the Pager Duty service. |  [optional] |
|**pagerDutyEventAction** | **String** | The event action for the Pager Duty service. |  |
|**pagerDutyPayloadClass** | **String** | The payload class for the Pager Duty service. |  [optional] |
|**pagerDutyPayloadComponent** | **String** | The payload component for the Pager Duty service. |  [optional] |
|**pagerDutyPayloadGroup** | **String** | The payload group for the Pager Duty service. |  [optional] |
|**pagerDutyPayloadSeverity** | **String** | The payload severity for the Pager Duty service. |  [optional] |
|**pagerDutyPayloadSource** | **String** | The payload source for the Pager Duty service. |  [optional] |
|**pagerDutyRoutingKey** | **String** | The routing key for the Pager Duty service. |  |
|**transportName** | **String** | The name of the transport. |  |



