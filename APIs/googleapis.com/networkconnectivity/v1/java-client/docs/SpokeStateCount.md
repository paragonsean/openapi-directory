

# SpokeStateCount

The number of spokes that are in a particular state and associated with a given hub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **String** | Output only. The total number of spokes that are in this state and associated with a given hub. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the spokes. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| ACCEPTING | &quot;ACCEPTING&quot; |
| REJECTING | &quot;REJECTING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| OBSOLETE | &quot;OBSOLETE&quot; |



