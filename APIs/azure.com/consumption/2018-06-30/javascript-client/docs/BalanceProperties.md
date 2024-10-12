# ConsumptionManagementClient.BalanceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustmentDetails** | [**[BalancePropertiesAdjustmentDetailsInner]**](BalancePropertiesAdjustmentDetailsInner.md) | List of Adjustments (Promo credit, SIE credit etc.). | [optional] [readonly] 
**adjustments** | **Number** | Total adjustment amount. | [optional] [readonly] 
**azureMarketplaceServiceCharges** | **Number** | Total charges for Azure Marketplace. | [optional] [readonly] 
**beginningBalance** | **Number** | The beginning balance for the billing period. | [optional] [readonly] 
**billingFrequency** | **String** | The billing frequency. | [optional] 
**chargesBilledSeparately** | **Number** | Charges Billed separately. | [optional] [readonly] 
**currency** | **String** | The ISO currency in which the meter is charged, for example, USD. | [optional] [readonly] 
**endingBalance** | **Number** | The ending balance for the billing period (for open periods this will be updated daily). | [optional] [readonly] 
**newPurchases** | **Number** | Total new purchase amount. | [optional] [readonly] 
**newPurchasesDetails** | [**[BalancePropertiesNewPurchasesDetailsInner]**](BalancePropertiesNewPurchasesDetailsInner.md) | List of new purchases. | [optional] [readonly] 
**priceHidden** | **Boolean** | Price is hidden or not. | [optional] [readonly] 
**serviceOverage** | **Number** | Overage for Azure services. | [optional] [readonly] 
**totalOverage** | **Number** | serviceOverage + chargesBilledSeparately. | [optional] [readonly] 
**totalUsage** | **Number** | Azure service commitment + total Overage. | [optional] [readonly] 
**utilized** | **Number** | Total Commitment usage. | [optional] [readonly] 



## Enum: BillingFrequencyEnum


* `Month` (value: `"Month"`)

* `Quarter` (value: `"Quarter"`)

* `Year` (value: `"Year"`)




