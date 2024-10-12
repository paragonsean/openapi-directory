# ProductFinderApi.SMELoanMarketingStateInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coreProduct** | **Object** | SME Loan core product details. | 
**eligibility** | **Object** | Eligibility details for this product i.e. the criteria that an business has to meet in order to be eligible for the SME Loan product. | 
**featuresAndBenefits** | **Object** | Feature And Benefits Details | 
**firstMarketedDate** | **Date** | Marketing state start date | [optional] 
**identification** | **String** | Unique and unambiguous identification of a  SME Loan Product Marketing State. | 
**lastMarketedDate** | **Date** | Marketing state end date | [optional] 
**loanInterest** | **Object** | Details about the interest that may be payable to the SME Loan | 
**marketingState** | **String** | Describes the marketing state (regular or promotional) of the SME Loan Product | 
**notes** | **[String]** | Free text for adding details for marketing state | [optional] 
**otherFeesCharges** | **Object** | Contains details of fees and charges which are not associated with either loan interest or repayments | [optional] 
**predecessorID** | **String** | Identifies the marketing state that precedes this marketing state | [optional] 
**repayment** | [**[RepaymentInner]**](RepaymentInner.md) | Repayment details of the Loan product | 
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




