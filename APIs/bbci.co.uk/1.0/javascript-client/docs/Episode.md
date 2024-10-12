# BbcIPlayerBusinessLayer.Episode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioDescribed** | **Boolean** |  | 
**categories** | **[String]** |  | 
**childrens** | **Boolean** |  | [optional] 
**editorialSubtitle** | **String** |  | [optional] 
**editorialTitle** | **String** |  | [optional] 
**eventGroupId** | **String** |  | [optional] 
**guidance** | **Boolean** |  | 
**hasCredits** | **Boolean** |  | [optional] 
**id** | **String** |  | 
**images** | [**EpisodeImages**](EpisodeImages.md) |  | 
**labels** | [**EpisodeLabels**](EpisodeLabels.md) |  | [optional] 
**lexicalSortLetter** | **String** |  | 
**live** | **Boolean** |  | [optional] 
**liveSubtitle** | **String** |  | [optional] 
**liveTitle** | **String** |  | [optional] 
**masterBrand** | [**MasterBrand**](MasterBrand.md) |  | 
**nextBroadcast** | [**EpisodeNextBroadcast**](EpisodeNextBroadcast.md) |  | [optional] 
**numericTleoPosition** | **Number** |  | [optional] 
**originalTitle** | **String** |  | [optional] 
**parentId** | **String** |  | [optional] 
**parentPosition** | **Number** |  | [optional] 
**previewId** | **String** |  | [optional] 
**programmeType** | **String** |  | [optional] 
**promoted** | **Boolean** |  | [optional] 
**relatedLinks** | [**[EpisodeRelatedLinksInner]**](EpisodeRelatedLinksInner.md) |  | [optional] 
**releaseDate** | **String** |  | [optional] 
**releaseDateTime** | **String** |  | [optional] 
**requiresAb** | **[String]** |  | [optional] 
**requiresSignIn** | **Boolean** |  | 
**requiresTvLicence** | **Boolean** |  | [optional] 
**signed** | **Boolean** |  | 
**sliceId** | **String** |  | [optional] 
**sliceSubtitle** | **String** |  | [optional] 
**status** | **String** |  | 
**subtitle** | **String** |  | [optional] 
**synopses** | [**EpisodeSynopses**](EpisodeSynopses.md) |  | 
**tests** | [**[EpisodeTestsInner]**](EpisodeTestsInner.md) |  | [optional] 
**title** | **String** |  | 
**tleoId** | **String** |  | 
**tleoType** | **String** |  | 
**type** | **String** |  | 
**versions** | [**[EpisodeVersionsInner]**](EpisodeVersionsInner.md) |  | 



## Enum: ProgrammeTypeEnum


* `narrative` (value: `"narrative"`)

* `sequential` (value: `"sequential"`)

* `self-contained` (value: `"self-contained"`)

* `strand` (value: `"strand"`)

* `unclassified` (value: `"unclassified"`)

* `one-off` (value: `"one-off"`)





## Enum: [RequiresAbEnum]


* `u13` (value: `"u13"`)

* `u16` (value: `"u16"`)

* `u18` (value: `"u18"`)

* `o18` (value: `"o18"`)





## Enum: StatusEnum


* `available` (value: `"available"`)

* `unavailable` (value: `"unavailable"`)





## Enum: TleoTypeEnum


* `episode` (value: `"episode"`)

* `brand` (value: `"brand"`)

* `series` (value: `"series"`)





## Enum: TypeEnum


* `episode` (value: `"episode"`)

* `episode_large` (value: `"episode_large"`)




