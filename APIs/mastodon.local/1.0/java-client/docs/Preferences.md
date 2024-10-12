

# Preferences

Represents a user's preferences.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postingColonDefaultColonLanguage** | **String** | Default language for new posts. Equivalent to [Source#language](https://docs.joinmastodon.org/entities/source/#language). ISO 639-1 language two-letter code, or null |  [optional] |
|**postingColonDefaultColonSensitive** | **Boolean** | Default sensitivity flag for new posts. Equivalent to [Source#sensitive](https://docs.joinmastodon.org/entities/source/#sensitive). |  [optional] |
|**postingColonDefaultColonVisibility** | [**PostingColonDefaultColonVisibilityEnum**](#PostingColonDefaultColonVisibilityEnum) | Default visibility for new posts. Equivalent to [Source#privacy](https://docs.joinmastodon.org/entities/source/#privacy). |  [optional] |
|**readingColonExpandColonMedia** | [**ReadingColonExpandColonMediaEnum**](#ReadingColonExpandColonMediaEnum) | Whether media attachments should be automatically displayed or blurred/hidden. |  [optional] |
|**readingColonExpandColonSpoilers** | **Boolean** | Whether CWs should be expanded by default. |  [optional] |



## Enum: PostingColonDefaultColonVisibilityEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| UNLISTED | &quot;unlisted&quot; |
| PRIVATE | &quot;private&quot; |
| DIRECT | &quot;direct&quot; |



## Enum: ReadingColonExpandColonMediaEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| SHOW_ALL | &quot;show_all&quot; |
| HIDE_ALL | &quot;hide_all&quot; |



