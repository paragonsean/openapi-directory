

# WritableCable


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**color** | **String** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**label** | **String** |  |  [optional] |
|**length** | **Integer** |  |  [optional] |
|**lengthUnit** | [**LengthUnitEnum**](#LengthUnitEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**terminationA** | **Map&lt;String, String&gt;** |  |  [optional] [readonly] |
|**terminationAId** | **Integer** |  |  |
|**terminationAType** | **String** |  |  |
|**terminationB** | **Map&lt;String, String&gt;** |  |  [optional] [readonly] |
|**terminationBId** | **Integer** |  |  |
|**terminationBType** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: LengthUnitEnum

| Name | Value |
|---- | -----|
| M | &quot;m&quot; |
| CM | &quot;cm&quot; |
| FT | &quot;ft&quot; |
| IN | &quot;in&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CONNECTED | &quot;connected&quot; |
| PLANNED | &quot;planned&quot; |
| DECOMMISSIONING | &quot;decommissioning&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAT3 | &quot;cat3&quot; |
| CAT5 | &quot;cat5&quot; |
| CAT5E | &quot;cat5e&quot; |
| CAT6 | &quot;cat6&quot; |
| CAT6A | &quot;cat6a&quot; |
| CAT7 | &quot;cat7&quot; |
| DAC_ACTIVE | &quot;dac-active&quot; |
| DAC_PASSIVE | &quot;dac-passive&quot; |
| MRJ21_TRUNK | &quot;mrj21-trunk&quot; |
| COAXIAL | &quot;coaxial&quot; |
| MMF | &quot;mmf&quot; |
| MMF_OM1 | &quot;mmf-om1&quot; |
| MMF_OM2 | &quot;mmf-om2&quot; |
| MMF_OM3 | &quot;mmf-om3&quot; |
| MMF_OM4 | &quot;mmf-om4&quot; |
| SMF | &quot;smf&quot; |
| SMF_OS1 | &quot;smf-os1&quot; |
| SMF_OS2 | &quot;smf-os2&quot; |
| AOC | &quot;aoc&quot; |
| POWER | &quot;power&quot; |



