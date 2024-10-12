# ContentApiForShopping.CustomAttribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the attribute. Underscores will be replaced by spaces upon insertion. | [optional] 
**type** | **String** | The type of the attribute. Acceptable values are: - \&quot;&#x60;boolean&#x60;\&quot; - \&quot;&#x60;datetimerange&#x60;\&quot; - \&quot;&#x60;float&#x60;\&quot; - \&quot;&#x60;group&#x60;\&quot; - \&quot;&#x60;int&#x60;\&quot; - \&quot;&#x60;price&#x60;\&quot; - \&quot;&#x60;text&#x60;\&quot; - \&quot;&#x60;time&#x60;\&quot; - \&quot;&#x60;url&#x60;\&quot;  | [optional] 
**unit** | **String** | Free-form unit of the attribute. Unit can only be used for values of type int, float, or price. | [optional] 
**value** | **String** | The value of the attribute. | [optional] 


