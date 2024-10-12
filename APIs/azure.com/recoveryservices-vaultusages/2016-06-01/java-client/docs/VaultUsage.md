

# VaultUsage

Usages of a vault.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentValue** | **Long** | Current value of usage. |  [optional] |
|**limit** | **Long** | Limit of usage. |  [optional] |
|**name** | [**NameInfo**](NameInfo.md) |  |  [optional] |
|**nextResetTime** | **OffsetDateTime** | Next reset time of usage. |  [optional] |
|**quotaPeriod** | **String** | Quota period of usage. |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | Unit of the usage. |  [optional] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;Count&quot; |
| BYTES | &quot;Bytes&quot; |
| SECONDS | &quot;Seconds&quot; |
| PERCENT | &quot;Percent&quot; |
| COUNT_PER_SECOND | &quot;CountPerSecond&quot; |
| BYTES_PER_SECOND | &quot;BytesPerSecond&quot; |



