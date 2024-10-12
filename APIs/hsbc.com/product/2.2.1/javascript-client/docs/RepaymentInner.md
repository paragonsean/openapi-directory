# ProductFinderApi.RepaymentInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountType** | **String** | The repayment is for paying just the interest only or both interest and capital or bullet amount or balance to date etc | [optional] 
**notes** | **[String]** | Optional additional notes to supplement the Repayment | [optional] 
**otherAmountType** | **Object** | Other amount type which is not in the standard code list | [optional] 
**otherRepaymentFrequency** | **Object** | Other repayment frequency which is not in the standard code list | [optional] 
**otherRepaymentType** | **Object** | Other repayment type which is not in the standard code list | [optional] 
**repaymentFeeCharges** | **Object** | Applicable fee/charges for repayment such as prepayment, full early repayment or non repayment. | [optional] 
**repaymentFrequency** | **String** | Repayment frequency | [optional] 
**repaymentHoliday** | [**[RepaymentHolidayInner]**](RepaymentHolidayInner.md) | Details of capital repayment holiday if any | [optional] 
**repaymentType** | **String** | Repayment type | [optional] 



## Enum: AmountTypeEnum


* `BalanceToDate` (value: `"BalanceToDate"`)

* `Balloon` (value: `"Balloon"`)

* `CapitalAndInterest` (value: `"CapitalAndInterest"`)

* `FeeChargeCap` (value: `"FeeChargeCap"`)

* `InterestOnly` (value: `"InterestOnly"`)

* `Bullet` (value: `"Bullet"`)

* `Other` (value: `"Other"`)





## Enum: RepaymentFrequencyEnum


* `Daily` (value: `"Daily"`)

* `Flexible` (value: `"Flexible"`)

* `Fortnightly` (value: `"Fortnightly"`)

* `HalfYearly` (value: `"HalfYearly"`)

* `Monthly` (value: `"Monthly"`)

* `Other` (value: `"Other"`)

* `Quarterly` (value: `"Quarterly"`)

* `Weekly` (value: `"Weekly"`)

* `Yearly` (value: `"Yearly"`)





## Enum: RepaymentTypeEnum


* `Balloon` (value: `"Balloon"`)

* `Bullet` (value: `"Bullet"`)

* `CapitalAndInterest` (value: `"CapitalAndInterest"`)

* `CustomSchedule` (value: `"CustomSchedule"`)

* `EarlyRepayment` (value: `"EarlyRepayment"`)

* `FixedCapitalFullyAmortising` (value: `"FixedCapitalFullyAmortising"`)

* `FixedCapitalWithBullet` (value: `"FixedCapitalWithBullet"`)

* `FixedCapitalAndInterestReducingBalance` (value: `"FixedCapitalAndInterestReducingBalance"`)

* `InterestOnly` (value: `"InterestOnly"`)

* `PrepaymentFee` (value: `"PrepaymentFee"`)

* `RepaymentWithBullet` (value: `"RepaymentWithBullet"`)

* `StraightLineInterestOnly` (value: `"StraightLineInterestOnly"`)




