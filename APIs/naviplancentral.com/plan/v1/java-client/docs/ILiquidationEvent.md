

# ILiquidationEvent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstSaleDate** | [**Date**](Date.md) |  |  [optional] |
|**lastSaleDate** | [**Date**](Date.md) |  |  [optional] |
|**liquidationType** | [**LiquidationTypeEnum**](#LiquidationTypeEnum) |  |  [optional] [readonly] |
|**liquidationTypeDescription** | **String** |  |  [optional] [readonly] |
|**saleDatesDescription** | **String** |  |  [optional] [readonly] |



## Enum: LiquidationTypeEnum

| Name | Value |
|---- | -----|
| SELL_AT_PLAN_END | &quot;SellAtPlanEnd&quot; |
| SELL_ALL_ON_SPECIFIC_DATE | &quot;SellAllOnSpecificDate&quot; |
| SELL_IN_INSTALLMENTS | &quot;SellInInstallments&quot; |



