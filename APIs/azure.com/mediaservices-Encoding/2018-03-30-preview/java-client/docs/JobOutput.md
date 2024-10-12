

# JobOutput

Describes all the properties of a JobOutput.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | **String** | The discriminator for derived types. |  |
|**error** | [**JobError**](JobError.md) |  |  [optional] |
|**progress** | **Integer** | If the JobOutput is in a Processing state, this contains the job completion percentage.  The value is an estimate and not intended to be used to predict job completion times. To determine if the JobOutput is complete, use the State property. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Describes the state of the JobOutput. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CANCELED | &quot;Canceled&quot; |
| CANCELING | &quot;Canceling&quot; |
| ERROR | &quot;Error&quot; |
| FINISHED | &quot;Finished&quot; |
| PROCESSING | &quot;Processing&quot; |
| QUEUED | &quot;Queued&quot; |
| SCHEDULED | &quot;Scheduled&quot; |



