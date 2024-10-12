

# TransportOpsgeniePatch

The TransportOpsgenie resource is a collection of transports that carry dispatched alerts to the external Opsgenie service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**opsgenieAlias** | **String** | The alias for the Opsgenie service. |  [optional] |
|**opsgenieApiKey** | **String** | The API key for the Opsgenie service. Stored in encrypted format. |  |
|**opsgenieEntity** | **String** | The entity for the Opsgenie service. |  [optional] |
|**opsgenieNote** | **String** | The note for the Opsgenie service. |  [optional] |
|**opsgeniePriority** | **String** | The priority for the Opsgenie service. |  [optional] |
|**opsgenieUser** | **String** | The user for the Opsgenie service. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |



