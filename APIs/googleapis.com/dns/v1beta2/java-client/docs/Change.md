

# Change

A Change represents a set of ResourceRecordSet additions and deletions applied atomically to a ManagedZone. ResourceRecordSets within a ManagedZone are modified by creating a new Change element in the Changes collection. In turn the Changes collection also records the past modifications to the ResourceRecordSets in a ManagedZone. The current state of the ManagedZone is the sum effect of applying all Change elements in the Changes collection in sequence.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additions** | [**List&lt;ResourceRecordSet&gt;**](ResourceRecordSet.md) | Which ResourceRecordSets to add? |  [optional] |
|**deletions** | [**List&lt;ResourceRecordSet&gt;**](ResourceRecordSet.md) | Which ResourceRecordSets to remove? Must match existing data exactly. |  [optional] |
|**id** | **String** | Unique identifier for the resource; defined by the server (output only). |  [optional] |
|**isServing** | **Boolean** | If the DNS queries for the zone will be served. |  [optional] |
|**kind** | **String** |  |  [optional] |
|**startTime** | **String** | The time that this operation was started by the server (output only). This is in RFC3339 text format. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the operation (output only). A status of \&quot;done\&quot; means that the request to update the authoritative servers has been sent, but the servers might not be updated yet. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| DONE | &quot;done&quot; |



