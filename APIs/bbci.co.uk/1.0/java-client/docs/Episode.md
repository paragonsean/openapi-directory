

# Episode


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioDescribed** | **Boolean** |  |  |
|**categories** | **List&lt;String&gt;** |  |  |
|**childrens** | **Boolean** |  |  [optional] |
|**editorialSubtitle** | **String** |  |  [optional] |
|**editorialTitle** | **String** |  |  [optional] |
|**eventGroupId** | **String** |  |  [optional] |
|**guidance** | **Boolean** |  |  |
|**hasCredits** | **Boolean** |  |  [optional] |
|**id** | **String** |  |  |
|**images** | [**EpisodeImages**](EpisodeImages.md) |  |  |
|**labels** | [**EpisodeLabels**](EpisodeLabels.md) |  |  [optional] |
|**lexicalSortLetter** | **String** |  |  |
|**live** | **Boolean** |  |  [optional] |
|**liveSubtitle** | **String** |  |  [optional] |
|**liveTitle** | **String** |  |  [optional] |
|**masterBrand** | [**MasterBrand**](MasterBrand.md) |  |  |
|**nextBroadcast** | [**EpisodeNextBroadcast**](EpisodeNextBroadcast.md) |  |  [optional] |
|**numericTleoPosition** | **BigDecimal** |  |  [optional] |
|**originalTitle** | **String** |  |  [optional] |
|**parentId** | **String** |  |  [optional] |
|**parentPosition** | **BigDecimal** |  |  [optional] |
|**previewId** | **String** |  |  [optional] |
|**programmeType** | [**ProgrammeTypeEnum**](#ProgrammeTypeEnum) |  |  [optional] |
|**promoted** | **Boolean** |  |  [optional] |
|**relatedLinks** | [**List&lt;EpisodeRelatedLinksInner&gt;**](EpisodeRelatedLinksInner.md) |  |  [optional] |
|**releaseDate** | **String** |  |  [optional] |
|**releaseDateTime** | **String** |  |  [optional] |
|**requiresAb** | [**Set&lt;RequiresAbEnum&gt;**](#Set&lt;RequiresAbEnum&gt;) |  |  [optional] |
|**requiresSignIn** | **Boolean** |  |  |
|**requiresTvLicence** | **Boolean** |  |  [optional] |
|**signed** | **Boolean** |  |  |
|**sliceId** | **String** |  |  [optional] |
|**sliceSubtitle** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**subtitle** | **String** |  |  [optional] |
|**synopses** | [**EpisodeSynopses**](EpisodeSynopses.md) |  |  |
|**tests** | [**List&lt;EpisodeTestsInner&gt;**](EpisodeTestsInner.md) |  |  [optional] |
|**title** | **String** |  |  |
|**tleoId** | **String** |  |  |
|**tleoType** | [**TleoTypeEnum**](#TleoTypeEnum) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**versions** | [**List&lt;EpisodeVersionsInner&gt;**](EpisodeVersionsInner.md) |  |  |



## Enum: ProgrammeTypeEnum

| Name | Value |
|---- | -----|
| NARRATIVE | &quot;narrative&quot; |
| SEQUENTIAL | &quot;sequential&quot; |
| SELF_CONTAINED | &quot;self-contained&quot; |
| STRAND | &quot;strand&quot; |
| UNCLASSIFIED | &quot;unclassified&quot; |
| ONE_OFF | &quot;one-off&quot; |



## Enum: Set&lt;RequiresAbEnum&gt;

| Name | Value |
|---- | -----|
| U13 | &quot;u13&quot; |
| U16 | &quot;u16&quot; |
| U18 | &quot;u18&quot; |
| O18 | &quot;o18&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



## Enum: TleoTypeEnum

| Name | Value |
|---- | -----|
| EPISODE | &quot;episode&quot; |
| BRAND | &quot;brand&quot; |
| SERIES | &quot;series&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EPISODE | &quot;episode&quot; |
| EPISODE_LARGE | &quot;episode_large&quot; |



