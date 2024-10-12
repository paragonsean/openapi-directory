# FrankieFinancialApi.Plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefits** | [**Benefits**](Benefits.md) |  | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 
**contract** | [**Contract**](Contract.md) |  | [optional] 
**defaultOfferMessage** | **String** | Default Offer (DMO/VDO) text to be displayed for this plan | 
**directDebitRequired** | **Boolean** | Is payment by direct debit required in order to subscribe to this plan | 
**discounts** | [**PlanDiscounts**](PlanDiscounts.md) |  | [optional] 
**estimatedBaseCost** | **Number** | Estimated cost of this plan, based on the usage from the uploaded bill, with no conditional discounts applied. If this plan offers no conditional discounts the estimatedTotalCost and the estimatedBaseCost will be the same. | 
**estimatedSaving** | **Number** | The estimated saving the customer could have realised if they had been on this plan during the billing period | 
**estimatedTotalCost** | **Number** | Estimated cost of this plan, based on the usage from uploaded bill, with all conditional discounts applied. | 
**feesAndCharges** | [**Fees**](Fees.md) |  | [optional] 
**greenOptions** | [**NameValue**](NameValue.md) |  | [optional] 
**id** | **Number** | Unique identifier for this plan. This ID is passed when calling the switch API. | 
**name** | **String** | Name of the plan | 
**payOnTimeRequired** | **Boolean** | Is pay on time required in order to subscribe to this plan | 
**paymentOptions** | [**NameValue**](NameValue.md) |  | [optional] 
**rates** | [**Rates**](Rates.md) |  | 
**retailer** | [**Retailer**](Retailer.md) |  | 
**type** | **String** | The type of energy plan * &#x60;SR&#x60; - Single Rate * &#x60;TOU&#x60; - Time Of Use | 
**url** | **String** | Link to BPID (Basic Plan Information Document (NSW, SA, QLD, ACT)) or EPFS (Energy Price Fact Sheet (VIC)) | 



## Enum: TypeEnum


* `SR` (value: `"SR"`)

* `TOU` (value: `"TOU"`)




