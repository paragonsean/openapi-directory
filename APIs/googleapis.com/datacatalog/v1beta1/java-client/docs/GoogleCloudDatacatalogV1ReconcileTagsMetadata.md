

# GoogleCloudDatacatalogV1ReconcileTagsMetadata

Long-running operation metadata message returned by the ReconcileTags.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**Map&lt;String, Status&gt;**](Status.md) | Maps the name of each tagged column (or empty string for a sole entry) to tagging operation status. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the reconciliation operation. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;RECONCILIATION_STATE_UNSPECIFIED&quot; |
| QUEUED | &quot;RECONCILIATION_QUEUED&quot; |
| IN_PROGRESS | &quot;RECONCILIATION_IN_PROGRESS&quot; |
| DONE | &quot;RECONCILIATION_DONE&quot; |



