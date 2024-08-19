

# TflApiPresentationEntitiesStopPointSequence


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**branchId** | **Integer** | The id of this branch. |  [optional] |
|**direction** | **String** |  |  [optional] |
|**lineId** | **String** |  |  [optional] |
|**lineName** | **String** |  |  [optional] |
|**nextBranchIds** | **List&lt;Integer&gt;** | The ids of the next branch(es) in the sequence. Note that the next and previous branch id can be              identical in the case of a looped route e.g. the Circle line. |  [optional] |
|**prevBranchIds** | **List&lt;Integer&gt;** | The ids of the previous branch(es) in the sequence. Note that the next and previous branch id can be              identical in the case of a looped route e.g. the Circle line. |  [optional] |
|**serviceType** | [**ServiceTypeEnum**](#ServiceTypeEnum) |  |  [optional] |
|**stopPoint** | [**List&lt;TflApiPresentationEntitiesMatchedStop&gt;**](TflApiPresentationEntitiesMatchedStop.md) |  |  [optional] |



## Enum: ServiceTypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;Regular&quot; |
| NIGHT | &quot;Night&quot; |



