# CampaignManager360Api.TagSetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalKeyValues** | **String** | Additional key-values to be included in tags. Each key-value pair must be of the form key&#x3D;value, and pairs must be separated by a semicolon (;). Keys and values must not contain commas. For example, id&#x3D;2;color&#x3D;red is a valid value for this field. | [optional] 
**includeClickThroughUrls** | **Boolean** | Whether static landing page URLs should be included in the tags. This setting applies only to placements. | [optional] 
**includeClickTracking** | **Boolean** | Whether click-tracking string should be included in the tags. | [optional] 
**keywordOption** | **String** | Option specifying how keywords are embedded in ad tags. This setting can be used to specify whether keyword placeholders are inserted in placement tags for this site. Publishers can then add keywords to those placeholders. | [optional] 



## Enum: KeywordOptionEnum


* `PLACEHOLDER_WITH_LIST_OF_KEYWORDS` (value: `"PLACEHOLDER_WITH_LIST_OF_KEYWORDS"`)

* `IGNORE` (value: `"IGNORE"`)

* `GENERATE_SEPARATE_TAG_FOR_EACH_KEYWORD` (value: `"GENERATE_SEPARATE_TAG_FOR_EACH_KEYWORD"`)




