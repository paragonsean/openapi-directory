# ProductFinderApi.BCAMarketingStateInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coreProduct** | **Object** | BCA core product details. | [optional] 
**creditInterest** | **Object** | Details about the interest that may be payable to the BCA account holders | [optional] 
**eligibility** | **Object** | Eligibility details for this product i.e. the criteria that an accountholder has to meet in order to be eligible for the BCA product. | [optional] 
**featuresAndBenefits** | **Object** | Feature And Benefits Details | [optional] 
**firstMarketedDate** | **Date** | Marketing state start date | [optional] 
**identification** | **String** | Unique and unambiguous identification of a  BCA Product Marketing State. | 
**lastMarketedDate** | **Date** | Marketing state end date | [optional] 
**marketingState** | **String** | Describes the marketing state (regular or promotional) of the BCA Product | 
**notes** | **[String]** | Free text for adding details for marketing state | [optional] 
**otherFeesCharges** | [**[OtherFeesChargesInner]**](OtherFeesChargesInner.md) | Contains details of fees and charges which are not associated with either Overdraft or features/benefits | 
**overdraft** | **Object** | Borrowing details | [optional] 
**predecessorID** | **String** | Identifies the marketing state that precedes this marketing state | [optional] 
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

* `AcademicTerm` (value: `"AcademicTerm"`)

* `Year` (value: `"Year"`)




