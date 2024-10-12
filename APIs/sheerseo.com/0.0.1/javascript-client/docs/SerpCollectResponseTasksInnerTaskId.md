# SheerSeoApi.SerpCollectResponseTasksInnerTaskId

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorMessage** | **String** | error message in case task status is invalid | [optional] 
**keyword** | **String** | keyword (search term) | [optional] 
**localizationCode** | **String** | A code for the localization, which is a combination of country and language | [optional] 
**localizationZip** | **String** | option to localize the results per zip code | [optional] 
**numResults** | **Number** | number of results found in SERP | [optional] 
**organicResults** | [**[SerpCollectResponseTasksInnerTaskIdOrganicResultsInner]**](SerpCollectResponseTasksInnerTaskIdOrganicResultsInner.md) |  | [optional] 
**ready** | **String** | task ready indicator | [optional] 
**searchEngine** | **String** |  | [optional] 
**status** | **String** | task status in terms of success | [optional] 



## Enum: LocalizationCodeEnum


* `us` (value: `"us"`)

* `uk` (value: `"uk"`)

* `au` (value: `"au"`)

* `br` (value: `"br"`)

* `be_dutch` (value: `"be_dutch"`)

* `be_french` (value: `"be_french"`)

* `ca` (value: `"ca"`)

* `de` (value: `"de"`)

* `es` (value: `"es"`)

* `ie` (value: `"ie"`)

* `il` (value: `"il"`)

* `nl` (value: `"nl"`)

* `sg` (value: `"sg"`)

* `za` (value: `"za"`)

* `it` (value: `"it"`)

* `is` (value: `"is"`)

* `ch` (value: `"ch"`)

* `fr` (value: `"fr"`)

* `se` (value: `"se"`)

* `at` (value: `"at"`)

* `dk` (value: `"dk"`)

* `nz` (value: `"nz"`)

* `gr` (value: `"gr"`)

* `in` (value: `"in"`)

* `ms` (value: `"ms"`)

* `pl` (value: `"pl"`)

* `hk` (value: `"hk"`)

* `id` (value: `"id"`)

* `ru` (value: `"ru"`)

* `ae` (value: `"ae"`)

* `fi` (value: `"fi"`)

* `pt` (value: `"pt"`)

* `mx` (value: `"mx"`)

* `tr` (value: `"tr"`)

* `cl` (value: `"cl"`)

* `jp` (value: `"jp"`)

* `ar` (value: `"ar"`)





## Enum: ReadyEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)





## Enum: StatusEnum


* `ok` (value: `"ok"`)

* `invalid` (value: `"invalid"`)




