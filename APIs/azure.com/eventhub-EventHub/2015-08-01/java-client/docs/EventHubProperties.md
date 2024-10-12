

# EventHubProperties

Properties supplied to the Create Or Update Event Hub operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Exact time the Event Hub was created. |  [optional] [readonly] |
|**messageRetentionInDays** | **Long** | Number of days to retain the events for this Event Hub. |  [optional] |
|**partitionCount** | **Long** | Number of partitions created for the Event Hub. |  [optional] |
|**partitionIds** | **List&lt;String&gt;** | Current number of shards on the Event Hub. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Enumerates the possible values for the status of the Event Hub. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The exact time the message was updated. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| DISABLED | &quot;Disabled&quot; |
| RESTORING | &quot;Restoring&quot; |
| SEND_DISABLED | &quot;SendDisabled&quot; |
| RECEIVE_DISABLED | &quot;ReceiveDisabled&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| RENAMING | &quot;Renaming&quot; |
| UNKNOWN | &quot;Unknown&quot; |



