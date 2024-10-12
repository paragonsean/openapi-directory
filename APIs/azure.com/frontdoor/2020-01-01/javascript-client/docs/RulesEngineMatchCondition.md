# FrontDoorManagementClient.RulesEngineMatchCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**negateCondition** | **Boolean** | Describes if this is negate condition or not | [optional] 
**rulesEngineMatchValue** | **[String]** | Match values to match against. The operator will apply to each value in here with OR semantics. If any of them match the variable with the given operator this match condition is considered a match. | 
**rulesEngineMatchVariable** | **String** | Match Variable | 
**rulesEngineOperator** | **String** | Describes operator to apply to the match condition. | 
**selector** | **String** | Name of selector in RequestHeader or RequestBody to be matched | [optional] 
**transforms** | [**[Transform]**](Transform.md) | List of transforms | [optional] 



## Enum: RulesEngineMatchVariableEnum


* `IsMobile` (value: `"IsMobile"`)

* `RemoteAddr` (value: `"RemoteAddr"`)

* `RequestMethod` (value: `"RequestMethod"`)

* `QueryString` (value: `"QueryString"`)

* `PostArgs` (value: `"PostArgs"`)

* `RequestUri` (value: `"RequestUri"`)

* `RequestPath` (value: `"RequestPath"`)

* `RequestFilename` (value: `"RequestFilename"`)

* `RequestFilenameExtension` (value: `"RequestFilenameExtension"`)

* `RequestHeader` (value: `"RequestHeader"`)

* `RequestBody` (value: `"RequestBody"`)

* `RequestScheme` (value: `"RequestScheme"`)





## Enum: RulesEngineOperatorEnum


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




