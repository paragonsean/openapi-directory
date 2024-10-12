# ProductFinderApi.PCAMarketingStateInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coreProduct** | **Object** | Core feature of the PCA product which can be associated to a particular Marketing State | [optional] 
**creditInterest** | **Object** | Details about the interest that may be payable to the PCA account holders | [optional] 
**eligibility** | **Object** | Eligibility details for this product i.e. the criteria that an accountholder has to meet in order to be eligible for the PCA product. | [optional] 
**featuresAndBenefits** | **Object** | Feature And Benefits Details | [optional] 
**firstMarketedDate** | **Date** | Marketing state start date | [optional] 
**identification** | **String** | Unique and unambiguous identification of a  Eligibility Marketing state. | 
**lastMarketedDate** | **Date** | Marketing state end date | [optional] 
**marketingState** | **String** | Describes the marketing state (regular or promotional) for which the eligibility criteria applies | 
**notes** | **[String]** | Free text for adding details for marketing state | [optional] 
**otherFeesCharges** | **Object** | Contains details of fees and charges which are not associated with either borrowing or features/benefits | 
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




