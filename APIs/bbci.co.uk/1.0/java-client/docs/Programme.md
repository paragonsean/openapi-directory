

# Programme


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categories** | **List&lt;String&gt;** |  |  |
|**count** | **BigDecimal** |  |  |
|**id** | **String** |  |  |
|**images** | [**ClipImages**](ClipImages.md) |  |  |
|**initialChildren** | [**List&lt;Episode&gt;**](Episode.md) |  |  |
|**labels** | [**ProgrammeLabels**](ProgrammeLabels.md) |  |  [optional] |
|**lexicalSortLetter** | **String** |  |  |
|**masterBrand** | [**MasterBrand**](MasterBrand.md) |  |  |
|**programmeType** | [**ProgrammeTypeEnum**](#ProgrammeTypeEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**synopses** | [**ClipVersionsInnerGuidanceText**](ClipVersionsInnerGuidanceText.md) |  |  |
|**title** | **String** |  |  |
|**tleoType** | [**TleoTypeEnum**](#TleoTypeEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: ProgrammeTypeEnum

| Name | Value |
|---- | -----|
| NARRATIVE | &quot;narrative&quot; |
| SEQUENTIAL | &quot;sequential&quot; |
| SELF_CONTAINED | &quot;self-contained&quot; |
| STRAND | &quot;strand&quot; |
| UNCLASSIFIED | &quot;unclassified&quot; |
| ONE_OFF | &quot;one-off&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



## Enum: TleoTypeEnum

| Name | Value |
|---- | -----|
| BRAND | &quot;brand&quot; |
| SERIES | &quot;series&quot; |
| EPISODE | &quot;episode&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PROGRAMME | &quot;programme&quot; |
| PROGRAMME_LARGE | &quot;programme_large&quot; |



