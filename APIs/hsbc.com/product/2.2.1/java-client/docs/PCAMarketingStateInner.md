

# PCAMarketingStateInner

Describes the type of the known state (regular, promotional )  of the product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coreProduct** | **Object** | Core feature of the PCA product which can be associated to a particular Marketing State |  [optional] |
|**creditInterest** | **Object** | Details about the interest that may be payable to the PCA account holders |  [optional] |
|**eligibility** | **Object** | Eligibility details for this product i.e. the criteria that an accountholder has to meet in order to be eligible for the PCA product. |  [optional] |
|**featuresAndBenefits** | **Object** | Feature And Benefits Details |  [optional] |
|**firstMarketedDate** | **LocalDate** | Marketing state start date |  [optional] |
|**identification** | **String** | Unique and unambiguous identification of a  Eligibility Marketing state. |  |
|**lastMarketedDate** | **LocalDate** | Marketing state end date |  [optional] |
|**marketingState** | [**MarketingStateEnum**](#MarketingStateEnum) | Describes the marketing state (regular or promotional) for which the eligibility criteria applies |  |
|**notes** | **List&lt;String&gt;** | Free text for adding details for marketing state |  [optional] |
|**otherFeesCharges** | **Object** | Contains details of fees and charges which are not associated with either borrowing or features/benefits |  |
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



