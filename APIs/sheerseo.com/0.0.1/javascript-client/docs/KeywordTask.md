# SheerSeoApi.KeywordTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **String** | keyword (search term) | 
**localizationCode** | **String** | A code for the localization, which is a combination of country and language | 
**localizationZip** | **String** | option to localize the results per zip code | [optional] 
**searchEngine** | **String** | google/bing/google_mobile | [optional] 
**status** | **String** | status of this task request. \&quot;ok\&quot; means we&#39;re working on collecting it. \&quot;invalid\&quot; means there was an error and it won&#39;t be collected | [optional] 
**taskId** | **String** | the assigned task id for this task. Should be used later in the serp-collect request | [optional] 



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





## Enum: SearchEngineEnum


* `google` (value: `"google"`)

* `bing` (value: `"bing"`)

* `google_mobile` (value: `"google_mobile"`)





## Enum: StatusEnum


* `ok` (value: `"ok"`)

* `invalid` (value: `"invalid"`)




