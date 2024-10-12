

# Activity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityAt** | **Long** | Unix epoch time |  [optional] |
|**id** | **Long** |  |  [optional] |
|**links** | [**ActivityLinks**](ActivityLinks.md) |  |  [optional] |
|**sourceText** | **String** | Source text |  [optional] |
|**targetText** | **String** | Target text of the activity, which is actually the translation of the source text. |  [optional] |
|**translator** | **Long** | Unique identifier of the translator/proofreader of this activity. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Currently there are two available activity types; &#39;translated&#39;, &#39;proofread&#39;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TRANSLATED | &quot;translated&quot; |
| PROOFREAD | &quot;proofread&quot; |



