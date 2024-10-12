

# SMELoanMarketingStateInner

The marketing state (promotional or regular) of the SME Loan Product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coreProduct** | **Object** | SME Loan core product details. |  |
|**eligibility** | **Object** | Eligibility details for this product i.e. the criteria that an business has to meet in order to be eligible for the SME Loan product. |  |
|**featuresAndBenefits** | **Object** | Feature And Benefits Details |  |
|**firstMarketedDate** | **LocalDate** | Marketing state start date |  [optional] |
|**identification** | **String** | Unique and unambiguous identification of a  SME Loan Product Marketing State. |  |
|**lastMarketedDate** | **LocalDate** | Marketing state end date |  [optional] |
|**loanInterest** | **Object** | Details about the interest that may be payable to the SME Loan |  |
|**marketingState** | [**MarketingStateEnum**](#MarketingStateEnum) | Describes the marketing state (regular or promotional) of the SME Loan Product |  |
|**notes** | **List&lt;String&gt;** | Free text for adding details for marketing state |  [optional] |
|**otherFeesCharges** | **Object** | Contains details of fees and charges which are not associated with either loan interest or repayments |  [optional] |
|**predecessorID** | **String** | Identifies the marketing state that precedes this marketing state |  [optional] |
|**repayment** | [**List&lt;RepaymentInner&gt;**](RepaymentInner.md) | Repayment details of the Loan product |  |
|**stateTenureLength** | **Float** | The length/duration of a promotional state |  [optional] |
|**stateTenurePeriod** | [**StateTenurePeriodEnum**](#StateTenurePeriodEnum) | The unit of period (days, weeks, months etc.) of the promotional length |  [optional] |



## Enum: MarketingStateEnum

| Name | Value |
|---- | -----|
| PROMOTIONAL | &quot;Promotional&quot; |
| REGULAR | &quot;Regular&quot; |



## Enum: StateTenurePeriodEnum

| Name | Value |
|---- | -----|
| DAY | &quot;Day&quot; |
| HALF_YEAR | &quot;Half Year&quot; |
| MONTH | &quot;Month&quot; |
| QUARTER | &quot;Quarter&quot; |
| WEEK | &quot;Week&quot; |
| YEAR | &quot;Year&quot; |



