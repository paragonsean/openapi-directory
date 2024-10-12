

# ForecastPropertiesConfidenceLevelsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bound** | [**BoundEnum**](#BoundEnum) | The boundary of the percentage, values could be &#39;Upper&#39; or &#39;Lower&#39; |  [optional] |
|**percentage** | **BigDecimal** | The percentage level of the confidence |  [optional] [readonly] |
|**value** | **BigDecimal** | The amount of forecast within the percentage level |  [optional] [readonly] |



## Enum: BoundEnum

| Name | Value |
|---- | -----|
| UPPER | &quot;Upper&quot; |
| LOWER | &quot;Lower&quot; |



