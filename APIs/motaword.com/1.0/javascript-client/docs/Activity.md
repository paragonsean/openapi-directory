# MotaWordApi.Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityAt** | **Number** | Unix epoch time | [optional] 
**id** | **Number** |  | [optional] 
**links** | [**ActivityLinks**](ActivityLinks.md) |  | [optional] 
**sourceText** | **String** | Source text | [optional] 
**targetText** | **String** | Target text of the activity, which is actually the translation of the source text. | [optional] 
**translator** | **Number** | Unique identifier of the translator/proofreader of this activity. | [optional] 
**type** | **String** | Currently there are two available activity types; &#39;translated&#39;, &#39;proofread&#39;. | [optional] 



## Enum: TypeEnum


* `translated` (value: `"translated"`)

* `proofread` (value: `"proofread"`)




