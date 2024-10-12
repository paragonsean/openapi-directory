

# ConnectorEvent

Unify event that is supported on the connector. Events are delivered via Webhooks.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**downstreamEventType** | **String** | Downstream event type |  [optional] |
|**entityType** | **String** | Unify entity type |  [optional] |
|**eventSource** | [**EventSourceEnum**](#EventSourceEnum) | Unify event source |  [optional] |
|**eventType** | **String** | Unify event type |  [optional] |
|**resources** | **List&lt;String&gt;** |  |  [optional] |



## Enum: EventSourceEnum

| Name | Value |
|---- | -----|
| NATIVE | &quot;native&quot; |
| VIRTUAL | &quot;virtual&quot; |



