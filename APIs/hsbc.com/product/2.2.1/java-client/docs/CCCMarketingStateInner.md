

# CCCMarketingStateInner

The marketing state (promotional or regular) of the CCC Product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coreProduct** | **Object** | CCC core product details. |  |
|**eligibility** | **Object** | Eligibility details for this product i.e. the criteria that an accountholder has to meet in order to be eligible for the CCC product. |  |
|**featuresAndBenefits** | **Object** | Feature And Benefits Details |  |
|**firstMarketedDate** | **LocalDate** | Marketing state start date |  [optional] |
|**identification** | **String** | Unique and unambiguous identification of a  CCC Product Marketing State. |  |
|**lastMarketedDate** | **LocalDate** | Marketing state end date |  [optional] |
|**marketingState** | [**MarketingStateEnum**](#MarketingStateEnum) | Describes the marketing state (regular or promotional) of the CCC Product |  |
|**notes** | **List&lt;String&gt;** | Free text for adding details for marketing state |  [optional] |
|**otherFeesCharges** | **Object** | Contains details of fees and charges which are not associated with either NonRepayment or features/benefits |  |
|**predecessorID** | **String** | Identifies the marketing state that precedes this marketing state |  [optional] |
|**repayment** | **Object** | Repayment details of the CCC product |  [optional] |
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



