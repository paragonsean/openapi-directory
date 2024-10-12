

# RepaymentInner

Repayment details of the Loan product

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountType** | [**AmountTypeEnum**](#AmountTypeEnum) | The repayment is for paying just the interest only or both interest and capital or bullet amount or balance to date etc |  [optional] |
|**notes** | **List&lt;String&gt;** | Optional additional notes to supplement the Repayment |  [optional] |
|**otherAmountType** | **Object** | Other amount type which is not in the standard code list |  [optional] |
|**otherRepaymentFrequency** | **Object** | Other repayment frequency which is not in the standard code list |  [optional] |
|**otherRepaymentType** | **Object** | Other repayment type which is not in the standard code list |  [optional] |
|**repaymentFeeCharges** | **Object** | Applicable fee/charges for repayment such as prepayment, full early repayment or non repayment. |  [optional] |
|**repaymentFrequency** | [**RepaymentFrequencyEnum**](#RepaymentFrequencyEnum) | Repayment frequency |  [optional] |
|**repaymentHoliday** | [**List&lt;RepaymentHolidayInner&gt;**](RepaymentHolidayInner.md) | Details of capital repayment holiday if any |  [optional] |
|**repaymentType** | [**RepaymentTypeEnum**](#RepaymentTypeEnum) | Repayment type |  [optional] |



## Enum: AmountTypeEnum

| Name | Value |
|---- | -----|
| BALANCE_TO_DATE | &quot;BalanceToDate&quot; |
| BALLOON | &quot;Balloon&quot; |
| CAPITAL_AND_INTEREST | &quot;CapitalAndInterest&quot; |
| FEE_CHARGE_CAP | &quot;FeeChargeCap&quot; |
| INTEREST_ONLY | &quot;InterestOnly&quot; |
| BULLET | &quot;Bullet&quot; |
| OTHER | &quot;Other&quot; |



## Enum: RepaymentFrequencyEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;Daily&quot; |
| FLEXIBLE | &quot;Flexible&quot; |
| FORTNIGHTLY | &quot;Fortnightly&quot; |
| HALF_YEARLY | &quot;HalfYearly&quot; |
| MONTHLY | &quot;Monthly&quot; |
| OTHER | &quot;Other&quot; |
| QUARTERLY | &quot;Quarterly&quot; |
| WEEKLY | &quot;Weekly&quot; |
| YEARLY | &quot;Yearly&quot; |



## Enum: RepaymentTypeEnum

| Name | Value |
|---- | -----|
| BALLOON | &quot;Balloon&quot; |
| BULLET | &quot;Bullet&quot; |
| CAPITAL_AND_INTEREST | &quot;CapitalAndInterest&quot; |
| CUSTOM_SCHEDULE | &quot;CustomSchedule&quot; |
| EARLY_REPAYMENT | &quot;EarlyRepayment&quot; |
| FIXED_CAPITAL_FULLY_AMORTISING | &quot;FixedCapitalFullyAmortising&quot; |
| FIXED_CAPITAL_WITH_BULLET | &quot;FixedCapitalWithBullet&quot; |
| FIXED_CAPITAL_AND_INTEREST_REDUCING_BALANCE | &quot;FixedCapitalAndInterestReducingBalance&quot; |
| INTEREST_ONLY | &quot;InterestOnly&quot; |
| PREPAYMENT_FEE | &quot;PrepaymentFee&quot; |
| REPAYMENT_WITH_BULLET | &quot;RepaymentWithBullet&quot; |
| STRAIGHT_LINE_INTEREST_ONLY | &quot;StraightLineInterestOnly&quot; |



