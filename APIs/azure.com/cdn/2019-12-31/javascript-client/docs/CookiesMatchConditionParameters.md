# CdnManagementClient.CookiesMatchConditionParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**odataType** | **String** |  | 
**matchValues** | **[String]** | The match value for the condition of the delivery rule | 
**negateCondition** | **Boolean** | Describes if this is negate condition or not | [optional] 
**operator** | **String** | Describes operator to be matched | 
**selector** | **String** | Name of Cookies to be matched | 
**transforms** | [**[Transform]**](Transform.md) | List of transforms | [optional] 



## Enum: OdataTypeEnum


* `#Microsoft.Azure.Cdn.Models.DeliveryRuleCookiesConditionParameters` (value: `"#Microsoft.Azure.Cdn.Models.DeliveryRuleCookiesConditionParameters"`)





## Enum: OperatorEnum


* `Any` (value: `"Any"`)

* `Equal` (value: `"Equal"`)

* `Contains` (value: `"Contains"`)

* `BeginsWith` (value: `"BeginsWith"`)

* `EndsWith` (value: `"EndsWith"`)

* `LessThan` (value: `"LessThan"`)

* `LessThanOrEqual` (value: `"LessThanOrEqual"`)

* `GreaterThan` (value: `"GreaterThan"`)

* `GreaterThanOrEqual` (value: `"GreaterThanOrEqual"`)




