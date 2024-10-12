

# FileRedundancyInformation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**expiresOn** | **OffsetDateTime** |  |  [optional] |
|**fileUrl** | **String** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**size** | **Integer** |  |  [optional] |
|**strategy** | [**StrategyEnum**](#StrategyEnum) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StrategyEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;manual&quot; |
| MOST_VIEWS | &quot;most-views&quot; |
| TRENDING | &quot;trending&quot; |
| RECENTLY_ADDED | &quot;recently-added&quot; |



