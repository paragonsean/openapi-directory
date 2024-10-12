

# RequestSchemeMatchConditionParameters

Defines the parameters for RequestScheme match conditions 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | [**AtOdataTypeEnum**](#AtOdataTypeEnum) |  |  |
|**matchValues** | [**List&lt;MatchValuesEnum&gt;**](#List&lt;MatchValuesEnum&gt;) | The match value for the condition of the delivery rule |  |
|**negateCondition** | **Boolean** | Describes if this is negate condition or not |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Describes operator to be matched |  |



## Enum: AtOdataTypeEnum

| Name | Value |
|---- | -----|
| _MICROSOFT_AZURE_CDN_MODELS_DELIVERY_RULE_REQUEST_SCHEME_CONDITION_PARAMETERS | &quot;#Microsoft.Azure.Cdn.Models.DeliveryRuleRequestSchemeConditionParameters&quot; |



## Enum: List&lt;MatchValuesEnum&gt;

| Name | Value |
|---- | -----|
| HTTP | &quot;HTTP&quot; |
| HTTPS | &quot;HTTPS&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| EQUAL | &quot;Equal&quot; |



