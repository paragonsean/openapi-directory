

# BadgeExpiry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expirationDate** | **OffsetDateTime** |  |  [optional] |
|**expires** | **Boolean** |  |  [optional] |
|**expiryType** | [**ExpiryTypeEnum**](#ExpiryTypeEnum) |  |  [optional] |
|**timeframeAmount** | **BigDecimal** |  |  [optional] |
|**timeframeUnit** | [**TimeframeUnitEnum**](#TimeframeUnitEnum) |  |  [optional] |



## Enum: ExpiryTypeEnum

| Name | Value |
|---- | -----|
| DATE | &quot;date&quot; |
| TIMEFRAME | &quot;timeframe&quot; |



## Enum: TimeframeUnitEnum

| Name | Value |
|---- | -----|
| DAYS | &quot;days&quot; |
| MONTHS | &quot;months&quot; |
| YEARS | &quot;years&quot; |



