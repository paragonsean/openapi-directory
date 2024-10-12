# ProductFinderApi.CCCMarketingStateInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coreProduct** | **Object** | CCC core product details. | 
**eligibility** | **Object** | Eligibility details for this product i.e. the criteria that an accountholder has to meet in order to be eligible for the CCC product. | 
**featuresAndBenefits** | **Object** | Feature And Benefits Details | 
**firstMarketedDate** | **Date** | Marketing state start date | [optional] 
**identification** | **String** | Unique and unambiguous identification of a  CCC Product Marketing State. | 
**lastMarketedDate** | **Date** | Marketing state end date | [optional] 
**marketingState** | **String** | Describes the marketing state (regular or promotional) of the CCC Product | 
**notes** | **[String]** | Free text for adding details for marketing state | [optional] 
**otherFeesCharges** | **Object** | Contains details of fees and charges which are not associated with either NonRepayment or features/benefits | 
**predecessorID** | **String** | Identifies the marketing state that precedes this marketing state | [optional] 
**repayment** | **Object** | Repayment details of the CCC product | [optional] 
**stateTenureLength** | **Number** | The length/duration of a promotional state | [optional] 
**stateTenurePeriod** | **String** | The unit of period (days, weeks, months etc.) of the promotional length | [optional] 



## Enum: MarketingStateEnum


* `Promotional` (value: `"Promotional"`)

* `Regular` (value: `"Regular"`)





## Enum: StateTenurePeriodEnum


* `Day` (value: `"Day"`)

* `Half Year` (value: `"Half Year"`)

* `Month` (value: `"Month"`)

* `Quarter` (value: `"Quarter"`)

* `Week` (value: `"Week"`)

* `Year` (value: `"Year"`)




