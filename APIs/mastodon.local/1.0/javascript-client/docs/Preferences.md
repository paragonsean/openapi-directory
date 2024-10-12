# MastodonApiSpecificationHttpsGithubComMastodonMastodon.Preferences

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postingdefaultlanguage** | **String** | Default language for new posts. Equivalent to [Source#language](https://docs.joinmastodon.org/entities/source/#language). ISO 639-1 language two-letter code, or null | [optional] 
**postingdefaultsensitive** | **Boolean** | Default sensitivity flag for new posts. Equivalent to [Source#sensitive](https://docs.joinmastodon.org/entities/source/#sensitive). | [optional] 
**postingdefaultvisibility** | **String** | Default visibility for new posts. Equivalent to [Source#privacy](https://docs.joinmastodon.org/entities/source/#privacy). | [optional] 
**readingexpandmedia** | **String** | Whether media attachments should be automatically displayed or blurred/hidden. | [optional] 
**readingexpandspoilers** | **Boolean** | Whether CWs should be expanded by default. | [optional] 



## Enum: PostingdefaultvisibilityEnum


* `public` (value: `"public"`)

* `unlisted` (value: `"unlisted"`)

* `private` (value: `"private"`)

* `direct` (value: `"direct"`)





## Enum: ReadingexpandmediaEnum


* `default` (value: `"default"`)

* `show_all` (value: `"show_all"`)

* `hide_all` (value: `"hide_all"`)




