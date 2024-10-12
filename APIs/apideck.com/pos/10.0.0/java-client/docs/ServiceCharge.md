

# ServiceCharge


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** |  |  [optional] |
|**amount** | **BigDecimal** |  |  [optional] |
|**currency** | **Currency** |  |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**name** | **String** | Service charge name |  [optional] |
|**percentage** | **BigDecimal** | Service charge percentage. Use this field to calculate the amount of the service charge. Pass a percentage and amount at the same time. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the service charge. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AUTO_GRATUITY | &quot;auto_gratuity&quot; |
| CUSTOM | &quot;custom&quot; |



