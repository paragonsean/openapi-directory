

# CurrentBillData

Data from uploaded bill

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountAddress** | **String** | Account (Billing) address. |  |
|**accountName** | **String** | Customer name. |  |
|**accountNumber** | **String** | Customer account number |  |
|**actualPlanTotalCost** | **BigDecimal** | Recalculated cost of the plan based on users comsumption and plan rates including discounts, rebates, concessions etc... Additional fees such as credit card processing fees are ignored. |  |
|**billDateFrom** | **String** | Start date for billing period |  |
|**billDateTo** | **String** | End date for billing period |  |
|**days** | **Integer** | Number of days in billing period (billDateTo - billDateFrom) |  |
|**discount** | **BigDecimal** | Total value of all unconditional discounts applied to the bill |  |
|**fuelType** | [**FuelTypeEnum**](#FuelTypeEnum) | * &#x60;E&#x60; - Electricity  |  |
|**nmi** | **String** | National Meter identifier (NMI) |  |
|**periods** | [**List&lt;Period&gt;**](Period.md) | Rates and charges for each period on the bill |  |
|**retailer** | [**Retailer**](Retailer.md) |  |  |
|**solar** | [**List&lt;CurrentBillDataSolarInner&gt;**](CurrentBillDataSolarInner.md) | Array of rates and charges for solar on the bill, by period. If no solar is present on the uploaded bill this object will not be present. |  [optional] |
|**supplyAddress** | **String** | Supply address. This may differ from account address if bill payers address is different from account address. |  |



## Enum: FuelTypeEnum

| Name | Value |
|---- | -----|
| E | &quot;E&quot; |



