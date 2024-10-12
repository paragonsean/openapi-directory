

# BalanceProperties

The properties of the balance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustmentDetails** | [**List&lt;BalancePropertiesAdjustmentDetailsInner&gt;**](BalancePropertiesAdjustmentDetailsInner.md) | List of Adjustments (Promo credit, SIE credit etc.). |  [optional] [readonly] |
|**adjustments** | **BigDecimal** | Total adjustment amount. |  [optional] [readonly] |
|**azureMarketplaceServiceCharges** | **BigDecimal** | Total charges for Azure Marketplace. |  [optional] [readonly] |
|**beginningBalance** | **BigDecimal** | The beginning balance for the billing period. |  [optional] [readonly] |
|**billingFrequency** | [**BillingFrequencyEnum**](#BillingFrequencyEnum) | The billing frequency. |  [optional] |
|**chargesBilledSeparately** | **BigDecimal** | Charges Billed separately. |  [optional] [readonly] |
|**currency** | **String** | The ISO currency in which the meter is charged, for example, USD. |  [optional] [readonly] |
|**endingBalance** | **BigDecimal** | The ending balance for the billing period (for open periods this will be updated daily). |  [optional] [readonly] |
|**newPurchases** | **BigDecimal** | Total new purchase amount. |  [optional] [readonly] |
|**newPurchasesDetails** | [**List&lt;BalancePropertiesNewPurchasesDetailsInner&gt;**](BalancePropertiesNewPurchasesDetailsInner.md) | List of new purchases. |  [optional] [readonly] |
|**priceHidden** | **Boolean** | Price is hidden or not. |  [optional] [readonly] |
|**serviceOverage** | **BigDecimal** | Overage for Azure services. |  [optional] [readonly] |
|**totalOverage** | **BigDecimal** | serviceOverage + chargesBilledSeparately. |  [optional] [readonly] |
|**totalUsage** | **BigDecimal** | Azure service commitment + total Overage. |  [optional] [readonly] |
|**utilized** | **BigDecimal** | Total Commitment usage. |  [optional] [readonly] |



## Enum: BillingFrequencyEnum

| Name | Value |
|---- | -----|
| MONTH | &quot;Month&quot; |
| QUARTER | &quot;Quarter&quot; |
| YEAR | &quot;Year&quot; |



