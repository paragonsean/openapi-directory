

# AddVideoToVodRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buy** | [**AddVideoToVodRequestBuy**](AddVideoToVodRequestBuy.md) |  |  [optional] |
|**position** | **BigDecimal** | The position of this video in the On Demand collection. |  [optional] |
|**releaseYear** | **BigDecimal** | The video release year. |  [optional] |
|**rent** | [**AddVideoToVodRequestRent**](AddVideoToVodRequestRent.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of video that you are adding to the On Demand page. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EXTRA | &quot;extra&quot; |
| MAIN | &quot;main&quot; |
| TRAILER | &quot;trailer&quot; |



