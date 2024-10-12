

# CreateVodAlt1RequestRent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Whether the video can be rented. *Required if &#x60;buy.active&#x60; is false. |  [optional] |
|**period** | [**PeriodEnum**](#PeriodEnum) | The period in which this can be rented for. |  [optional] |
|**price** | [**CreateVodAlt1RequestRentPrice**](CreateVodAlt1RequestRentPrice.md) |  |  [optional] |



## Enum: PeriodEnum

| Name | Value |
|---- | -----|
| _1_WEEK | &quot;1 week&quot; |
| _1_YEAR | &quot;1 year&quot; |
| _24_HOUR | &quot;24 hour&quot; |
| _3_MONTH | &quot;3 month&quot; |
| _30_DAY | &quot;30 day&quot; |
| _48_HOUR | &quot;48 hour&quot; |
| _6_MONTH | &quot;6 month&quot; |
| _72_HOUR | &quot;72 hour&quot; |



