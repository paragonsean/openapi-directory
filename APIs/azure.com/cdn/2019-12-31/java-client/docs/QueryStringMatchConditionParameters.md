

# QueryStringMatchConditionParameters

Defines the parameters for QueryString match conditions

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | [**AtOdataTypeEnum**](#AtOdataTypeEnum) |  |  |
|**matchValues** | **List&lt;String&gt;** | The match value for the condition of the delivery rule |  |
|**negateCondition** | **Boolean** | Describes if this is negate condition or not |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Describes operator to be matched |  |
|**transforms** | **List&lt;Transform&gt;** | List of transforms |  [optional] |



## Enum: AtOdataTypeEnum

| Name | Value |
|---- | -----|
| _MICROSOFT_AZURE_CDN_MODELS_DELIVERY_RULE_QUERY_STRING_CONDITION_PARAMETERS | &quot;#Microsoft.Azure.Cdn.Models.DeliveryRuleQueryStringConditionParameters&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| ANY | &quot;Any&quot; |
| EQUAL | &quot;Equal&quot; |
| CONTAINS | &quot;Contains&quot; |
| BEGINS_WITH | &quot;BeginsWith&quot; |
| ENDS_WITH | &quot;EndsWith&quot; |
| LESS_THAN | &quot;LessThan&quot; |
| LESS_THAN_OR_EQUAL | &quot;LessThanOrEqual&quot; |
| GREATER_THAN | &quot;GreaterThan&quot; |
| GREATER_THAN_OR_EQUAL | &quot;GreaterThanOrEqual&quot; |



