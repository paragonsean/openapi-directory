

# ModelFieldConfigValue


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** |  |  [optional] |
|**_enum** | **Set&lt;String&gt;** |  |  [optional] |
|**maxLength** | **Integer** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**fields** | [**Map&lt;String, ModelFieldConfigValueOneOf&gt;**](ModelFieldConfigValueOneOf.md) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AMOUNT | &quot;amount&quot; |
| DATE | &quot;date&quot; |
| DIGITS | &quot;digits&quot; |
| ENUM | &quot;enum&quot; |
| NUMERIC | &quot;numeric&quot; |
| STRING | &quot;string&quot; |
| LINES | &quot;lines&quot; |



