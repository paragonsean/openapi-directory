

# RequestMethodMatchConditionParameters

Defines the parameters for RequestMethod match conditions

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
| _MICROSOFT_AZURE_CDN_MODELS_DELIVERY_RULE_REQUEST_METHOD_CONDITION_PARAMETERS | &quot;#Microsoft.Azure.Cdn.Models.DeliveryRuleRequestMethodConditionParameters&quot; |



## Enum: List&lt;MatchValuesEnum&gt;

| Name | Value |
|---- | -----|
| GET | &quot;GET&quot; |
| HEAD | &quot;HEAD&quot; |
| POST | &quot;POST&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |
| OPTIONS | &quot;OPTIONS&quot; |
| TRACE | &quot;TRACE&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| EQUAL | &quot;Equal&quot; |



