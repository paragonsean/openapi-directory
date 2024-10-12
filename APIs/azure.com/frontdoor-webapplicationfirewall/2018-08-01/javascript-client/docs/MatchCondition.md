# WebApplicationFirewallManagement.MatchCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matchValue** | **[String]** | Match value | 
**matchVariable** | **String** | Match Variable | 
**negateCondition** | **Boolean** | Describes if this is negate condition or not | [optional] 
**operator** | **String** | Describes operator to be matched | 
**selector** | **String** | Name of selector in RequestHeader or RequestBody to be matched | [optional] 



## Enum: MatchVariableEnum


* `RemoteAddr` (value: `"RemoteAddr"`)

* `RequestMethod` (value: `"RequestMethod"`)

* `QueryString` (value: `"QueryString"`)

* `PostArgs` (value: `"PostArgs"`)

* `RequestUri` (value: `"RequestUri"`)

* `RequestHeader` (value: `"RequestHeader"`)

* `RequestBody` (value: `"RequestBody"`)





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




