

# Cable


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aTerminations** | [**List&lt;GenericObject&gt;**](GenericObject.md) |  |  [optional] |
|**bTerminations** | [**List&lt;GenericObject&gt;**](GenericObject.md) |  |  [optional] |
|**color** | **String** |  |  [optional] |
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**label** | **String** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**length** | **BigDecimal** |  |  [optional] |
|**lengthUnit** | [**LengthUnit**](LengthUnit.md) |  |  [optional] |
|**status** | [**Status**](Status.md) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | [**NestedTenant**](NestedTenant.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAT3 | &quot;cat3&quot; |
| CAT5 | &quot;cat5&quot; |
| CAT5E | &quot;cat5e&quot; |
| CAT6 | &quot;cat6&quot; |
| CAT6A | &quot;cat6a&quot; |
| CAT7 | &quot;cat7&quot; |
| CAT7A | &quot;cat7a&quot; |
| CAT8 | &quot;cat8&quot; |
| DAC_ACTIVE | &quot;dac-active&quot; |
| DAC_PASSIVE | &quot;dac-passive&quot; |
| MRJ21_TRUNK | &quot;mrj21-trunk&quot; |
| COAXIAL | &quot;coaxial&quot; |
| MMF | &quot;mmf&quot; |
| MMF_OM1 | &quot;mmf-om1&quot; |
| MMF_OM2 | &quot;mmf-om2&quot; |
| MMF_OM3 | &quot;mmf-om3&quot; |
| MMF_OM4 | &quot;mmf-om4&quot; |
| MMF_OM5 | &quot;mmf-om5&quot; |
| SMF | &quot;smf&quot; |
| SMF_OS1 | &quot;smf-os1&quot; |
| SMF_OS2 | &quot;smf-os2&quot; |
| AOC | &quot;aoc&quot; |
| POWER | &quot;power&quot; |



