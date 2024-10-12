

# RunnerDefinition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustmentFactor** | **Double** |  |  [optional] |
|**bsp** | **Double** |  |  [optional] |
|**hc** | **Double** | Handicap - the handicap of the runner (selection) (null if not applicable) |  [optional] |
|**id** | **Long** | Selection Id - the id of the runner (selection) |  [optional] |
|**removalDate** | **OffsetDateTime** |  |  [optional] |
|**sortPriority** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| WINNER | &quot;WINNER&quot; |
| LOSER | &quot;LOSER&quot; |
| REMOVED | &quot;REMOVED&quot; |
| REMOVED_VACANT | &quot;REMOVED_VACANT&quot; |
| HIDDEN | &quot;HIDDEN&quot; |
| PLACED | &quot;PLACED&quot; |



