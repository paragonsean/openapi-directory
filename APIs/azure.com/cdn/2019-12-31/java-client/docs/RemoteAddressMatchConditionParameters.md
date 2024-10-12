

# RemoteAddressMatchConditionParameters

Defines the parameters for RemoteAddress match conditions

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | [**AtOdataTypeEnum**](#AtOdataTypeEnum) |  |  |
|**matchValues** | **List&lt;String&gt;** | Match values to match against. The operator will apply to each value in here with OR semantics. If any of them match the variable with the given operator this match condition is considered a match. |  |
|**negateCondition** | **Boolean** | Describes if this is negate condition or not |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Describes operator to be matched |  |
|**transforms** | **List&lt;Transform&gt;** | List of transforms |  [optional] |



## Enum: AtOdataTypeEnum

| Name | Value |
|---- | -----|
| _MICROSOFT_AZURE_CDN_MODELS_DELIVERY_RULE_REMOTE_ADDRESS_CONDITION_PARAMETERS | &quot;#Microsoft.Azure.Cdn.Models.DeliveryRuleRemoteAddressConditionParameters&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| ANY | &quot;Any&quot; |
| IP_MATCH | &quot;IPMatch&quot; |
| GEO_MATCH | &quot;GeoMatch&quot; |



