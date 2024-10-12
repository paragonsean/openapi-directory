# CdnManagementClient.RemoteAddressMatchConditionParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**odataType** | **String** |  | 
**matchValues** | **[String]** | Match values to match against. The operator will apply to each value in here with OR semantics. If any of them match the variable with the given operator this match condition is considered a match. | 
**negateCondition** | **Boolean** | Describes if this is negate condition or not | [optional] 
**operator** | **String** | Describes operator to be matched | 
**transforms** | [**[Transform]**](Transform.md) | List of transforms | [optional] 



## Enum: OdataTypeEnum


* `#Microsoft.Azure.Cdn.Models.DeliveryRuleRemoteAddressConditionParameters` (value: `"#Microsoft.Azure.Cdn.Models.DeliveryRuleRemoteAddressConditionParameters"`)





## Enum: OperatorEnum


* `Any` (value: `"Any"`)

* `IPMatch` (value: `"IPMatch"`)

* `GeoMatch` (value: `"GeoMatch"`)




