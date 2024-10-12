

# HeaderActionParameters

Defines the parameters for the request header action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | [**AtOdataTypeEnum**](#AtOdataTypeEnum) |  |  |
|**headerAction** | [**HeaderActionEnum**](#HeaderActionEnum) | Action to perform |  |
|**headerName** | **String** | Name of the header to modify |  |
|**value** | **String** | Value for the specified action |  [optional] |



## Enum: AtOdataTypeEnum

| Name | Value |
|---- | -----|
| _MICROSOFT_AZURE_CDN_MODELS_DELIVERY_RULE_HEADER_ACTION_PARAMETERS | &quot;#Microsoft.Azure.Cdn.Models.DeliveryRuleHeaderActionParameters&quot; |



## Enum: HeaderActionEnum

| Name | Value |
|---- | -----|
| APPEND | &quot;Append&quot; |
| OVERWRITE | &quot;Overwrite&quot; |
| DELETE | &quot;Delete&quot; |



