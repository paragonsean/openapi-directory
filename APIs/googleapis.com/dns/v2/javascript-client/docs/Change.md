# CloudDnsApi.Change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | [**[ResourceRecordSet]**](ResourceRecordSet.md) | Which ResourceRecordSets to add? | [optional] 
**deletions** | [**[ResourceRecordSet]**](ResourceRecordSet.md) | Which ResourceRecordSets to remove? Must match existing data exactly. | [optional] 
**id** | **String** | Unique identifier for the resource; defined by the server (output only). | [optional] 
**isServing** | **Boolean** | If the DNS queries for the zone will be served. | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#change&#39;]
**startTime** | **String** | The time that this operation was started by the server (output only). This is in RFC3339 text format. | [optional] 
**status** | **String** | Status of the operation (output only). A status of \&quot;done\&quot; means that the request to update the authoritative servers has been sent, but the servers might not be updated yet. | [optional] 



## Enum: StatusEnum


* `PENDING` (value: `"PENDING"`)

* `DONE` (value: `"DONE"`)




