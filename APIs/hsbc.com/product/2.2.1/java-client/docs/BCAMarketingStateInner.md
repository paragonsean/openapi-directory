

# BCAMarketingStateInner

The marketing state (promotional or regular) of the BCA Product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coreProduct** | **Object** | BCA core product details. |  [optional] |
|**creditInterest** | **Object** | Details about the interest that may be payable to the BCA account holders |  [optional] |
|**eligibility** | **Object** | Eligibility details for this product i.e. the criteria that an accountholder has to meet in order to be eligible for the BCA product. |  [optional] |
|**featuresAndBenefits** | **Object** | Feature And Benefits Details |  [optional] |
|**firstMarketedDate** | **LocalDate** | Marketing state start date |  [optional] |
|**identification** | **String** | Unique and unambiguous identification of a  BCA Product Marketing State. |  |
|**lastMarketedDate** | **LocalDate** | Marketing state end date |  [optional] |
|**marketingState** | [**MarketingStateEnum**](#MarketingStateEnum) | Describes the marketing state (regular or promotional) of the BCA Product |  |
|**notes** | **List&lt;String&gt;** | Free text for adding details for marketing state |  [optional] |
|**otherFeesCharges** | [**List&lt;OtherFeesChargesInner&gt;**](OtherFeesChargesInner.md) | Contains details of fees and charges which are not associated with either Overdraft or features/benefits |  |
|**overdraft** | **Object** | Borrowing details |  [optional] |
|**predecessorID** | **String** | Identifies the marketing state that precedes this marketing state |  [optional] |
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
| ACADEMIC_TERM | &quot;AcademicTerm&quot; |
| YEAR | &quot;Year&quot; |



