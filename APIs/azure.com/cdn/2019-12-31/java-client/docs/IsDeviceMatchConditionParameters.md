

# IsDeviceMatchConditionParameters

Defines the parameters for IsDevice match conditions

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | [**AtOdataTypeEnum**](#AtOdataTypeEnum) |  |  |
|**matchValues** | [**List&lt;MatchValuesEnum&gt;**](#List&lt;MatchValuesEnum&gt;) | The match value for the condition of the delivery rule |  |
|**negateCondition** | **Boolean** | Describes if this is negate condition or not |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Describes operator to be matched |  |
|**transforms** | **List&lt;Transform&gt;** | List of transforms |  [optional] |



## Enum: AtOdataTypeEnum

| Name | Value |
|---- | -----|
| _MICROSOFT_AZURE_CDN_MODELS_DELIVERY_RULE_IS_DEVICE_CONDITION_PARAMETERS | &quot;#Microsoft.Azure.Cdn.Models.DeliveryRuleIsDeviceConditionParameters&quot; |



## Enum: List&lt;MatchValuesEnum&gt;

| Name | Value |
|---- | -----|
| MOBILE | &quot;Mobile&quot; |
| DESKTOP | &quot;Desktop&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| EQUAL | &quot;Equal&quot; |



