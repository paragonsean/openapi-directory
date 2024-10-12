# WebApplicationFirewallManagement.MatchCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matchValue** | **[String]** | List of possible match values. | 
**matchVariable** | **String** | Request variable to compare with. | 
**negateCondition** | **Boolean** | Describes if the result of this condition should be negated. | [optional] 
**operator** | **String** | Comparison type to use for matching with the variable value. | 
**selector** | **String** | Match against a specific key from the QueryString, PostArgs, RequestHeader or Cookies variables. Default is null. | [optional] 
**transforms** | [**[TransformType]**](TransformType.md) | List of transforms. | [optional] 



## Enum: MatchVariableEnum


* `RemoteAddr` (value: `"RemoteAddr"`)

* `RequestMethod` (value: `"RequestMethod"`)

* `QueryString` (value: `"QueryString"`)

* `PostArgs` (value: `"PostArgs"`)

* `RequestUri` (value: `"RequestUri"`)

* `RequestHeader` (value: `"RequestHeader"`)

* `RequestBody` (value: `"RequestBody"`)

* `Cookies` (value: `"Cookies"`)

* `SocketAddr` (value: `"SocketAddr"`)





## Enum: OperatorEnum


* `Any` (value: `"Any"`)

* `IPMatch` (value: `"IPMatch"`)

* `GeoMatch` (value: `"GeoMatch"`)

* `Equal` (value: `"Equal"`)

* `Contains` (value: `"Contains"`)

* `LessThan` (value: `"LessThan"`)

* `GreaterThan` (value: `"GreaterThan"`)

* `LessThanOrEqual` (value: `"LessThanOrEqual"`)

* `GreaterThanOrEqual` (value: `"GreaterThanOrEqual"`)

* `BeginsWith` (value: `"BeginsWith"`)

* `EndsWith` (value: `"EndsWith"`)

* `RegEx` (value: `"RegEx"`)




