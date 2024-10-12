

# ProductOptionFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** | Unique identifier of the product option |  [optional] |
|**name** | **String** | Name of the product option |  [optional] |
|**optionType** | [**OptionTypeEnum**](#OptionTypeEnum) | Type of the product option |  [optional] |
|**position** | **Integer** | Position of the product option |  [optional] |
|**values** | [**List&lt;ProductOptionValueFields&gt;**](ProductOptionValueFields.md) |  |  [optional] |



## Enum: OptionTypeEnum

| Name | Value |
|---- | -----|
| OPTION | &quot;option&quot; |
| INPUT | &quot;input&quot; |
| TEXT | &quot;text&quot; |
| FILE | &quot;file&quot; |



