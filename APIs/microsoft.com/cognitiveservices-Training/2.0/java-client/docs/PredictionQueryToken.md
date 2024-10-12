

# PredictionQueryToken


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**application** | **String** |  |  [optional] |
|**continuation** | **String** |  |  [optional] |
|**endTime** | **OffsetDateTime** |  |  [optional] |
|**iterationId** | **UUID** |  |  [optional] |
|**maxCount** | **Integer** |  |  [optional] |
|**orderBy** | [**OrderByEnum**](#OrderByEnum) |  |  [optional] |
|**session** | **String** |  |  [optional] |
|**startTime** | **OffsetDateTime** |  |  [optional] |
|**tags** | [**List&lt;PredictionQueryTag&gt;**](PredictionQueryTag.md) |  |  [optional] |



## Enum: OrderByEnum

| Name | Value |
|---- | -----|
| NEWEST | &quot;Newest&quot; |
| OLDEST | &quot;Oldest&quot; |
| SUGGESTED | &quot;Suggested&quot; |



