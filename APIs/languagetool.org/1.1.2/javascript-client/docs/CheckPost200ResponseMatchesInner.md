# LanguageToolApi.CheckPost200ResponseMatchesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**CheckPost200ResponseMatchesInnerContext**](CheckPost200ResponseMatchesInnerContext.md) |  | 
**length** | **Number** | The length of the error in characters. | 
**message** | **String** | Message about the error displayed to the user. | 
**offset** | **Number** | The 0-based character offset of the error in the text. | 
**replacements** | [**[CheckPost200ResponseMatchesInnerReplacementsInner]**](CheckPost200ResponseMatchesInnerReplacementsInner.md) | Replacements that might correct the error. The array can be empty, in this case there is no suggested replacement. | 
**rule** | [**CheckPost200ResponseMatchesInnerRule**](CheckPost200ResponseMatchesInnerRule.md) |  | [optional] 
**sentence** | **String** | The sentence the error occurred in (since LanguageTool 4.0 or later) | 
**shortMessage** | **String** | An optional shorter version of &#39;message&#39;. | [optional] 


