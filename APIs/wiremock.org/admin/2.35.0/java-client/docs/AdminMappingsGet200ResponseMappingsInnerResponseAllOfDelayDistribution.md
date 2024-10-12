

# AdminMappingsGet200ResponseMappingsInnerResponseAllOfDelayDistribution

The delay distribution. Valid property configuration is either median/sigma/type or lower/type/upper.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**median** | **Integer** |  |  [optional] |
|**sigma** | **BigDecimal** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**lower** | **Integer** |  |  [optional] |
|**upper** | **Integer** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LOGNORMAL | &quot;lognormal&quot; |
| UNIFORM | &quot;uniform&quot; |



