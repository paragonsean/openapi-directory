# NaviPlanApi.ILiability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annualPaymentAmount** | [**Currency**](Currency.md) |  | [optional] 
**balanceAsOf** | [**CurrencyWithDate**](CurrencyWithDate.md) |  | [optional] 
**balanceAsOfPlanDate** | [**Currency**](Currency.md) |  | [optional] 
**debtModStrategies** | [**IDebtModStrategies**](IDebtModStrategies.md) |  | [optional] 
**description** | **String** |  | [optional] [readonly] 
**id** | **String** |  | [optional] [readonly] 
**insuredForDisability** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  | [optional] 
**insuredForLife** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  | [optional] 
**interestRate** | [**Percent**](Percent.md) |  | [optional] 
**isInterestRateVariable** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  | [optional] 
**isPaymentVariable** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  | [optional] 
**linkedAssetId** | **String** |  | [optional] [readonly] 
**linkedAssetName** | **String** |  | [optional] [readonly] 
**loanDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**originalBalance** | [**Currency**](Currency.md) |  | [optional] 
**owner** | **String** |  | [optional] [readonly] 
**paidOffByRetirement** | [**IOptionalFieldDescriptiveBoolean**](IOptionalFieldDescriptiveBoolean.md) |  | [optional] 
**payOffDate** | [**IOptionalFieldDate**](IOptionalFieldDate.md) |  | [optional] 
**payOffOptionType** | [**FormattedEnumTypePayOffOptionsType**](FormattedEnumTypePayOffOptionsType.md) |  | [optional] 
**paymentAmount** | [**IOptionalFieldCurrency**](IOptionalFieldCurrency.md) |  | [optional] 
**paymentFrequency** | [**FormattedEnumTypeFrequency**](FormattedEnumTypeFrequency.md) |  | [optional] 
**paymentType** | [**FormattedEnumTypePaymentType**](FormattedEnumTypePaymentType.md) |  | [optional] 
**type** | [**FormattedEnumTypeLiabilityType**](FormattedEnumTypeLiabilityType.md) |  | [optional] 



## Enum: OwnerEnum


* `All` (value: `"All"`)

* `Head1` (value: `"Head1"`)

* `Head2` (value: `"Head2"`)

* `NonHead1` (value: `"NonHead1"`)

* `NonHead2` (value: `"NonHead2"`)

* `NonHead3` (value: `"NonHead3"`)

* `NonHead4` (value: `"NonHead4"`)

* `NonHead5` (value: `"NonHead5"`)

* `NonHead6` (value: `"NonHead6"`)

* `NonHead7` (value: `"NonHead7"`)

* `NonHead8` (value: `"NonHead8"`)

* `NonHead9` (value: `"NonHead9"`)

* `CommunityProperty` (value: `"CommunityProperty"`)

* `Joint` (value: `"Joint"`)

* `Other` (value: `"Other"`)

* `AllDependents` (value: `"AllDependents"`)

* `AllFamilyMembers` (value: `"AllFamilyMembers"`)

* `Corporation` (value: `"Corporation"`)




