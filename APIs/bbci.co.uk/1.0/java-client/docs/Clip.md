

# Clip


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**images** | [**ClipImages**](ClipImages.md) |  |  |
|**labels** | [**ClipLabels**](ClipLabels.md) |  |  [optional] |
|**masterBrand** | [**MasterBrand**](MasterBrand.md) |  |  |
|**onwardJourney** | [**ClipOnwardJourney**](ClipOnwardJourney.md) |  |  [optional] |
|**promotionType** | [**PromotionTypeEnum**](#PromotionTypeEnum) |  |  [optional] |
|**synopses** | [**ClipSynopses**](ClipSynopses.md) |  |  |
|**title** | **String** |  |  |
|**tleoId** | **String** |  |  |
|**tleoType** | [**TleoTypeEnum**](#TleoTypeEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**versions** | [**List&lt;ClipVersionsInner&gt;**](ClipVersionsInner.md) |  |  |



## Enum: PromotionTypeEnum

| Name | Value |
|---- | -----|
| AVAILABLE_NOW | &quot;available_now&quot; |
| COMING_SOON | &quot;coming_soon&quot; |



## Enum: TleoTypeEnum

| Name | Value |
|---- | -----|
| EPISODE | &quot;episode&quot; |
| BRAND | &quot;brand&quot; |
| SERIES | &quot;series&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CLIP | &quot;clip&quot; |



