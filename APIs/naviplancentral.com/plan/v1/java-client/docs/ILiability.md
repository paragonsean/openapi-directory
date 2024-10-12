

# ILiability


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annualPaymentAmount** | [**Currency**](Currency.md) |  |  [optional] |
|**balanceAsOf** | [**CurrencyWithDate**](CurrencyWithDate.md) |  |  [optional] |
|**balanceAsOfPlanDate** | [**Currency**](Currency.md) |  |  [optional] |
|**debtModStrategies** | [**IDebtModStrategies**](IDebtModStrategies.md) |  |  [optional] |
|**description** | **String** |  |  [optional] [readonly] |
|**id** | **String** |  |  [optional] [readonly] |
|**insuredForDisability** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  |  [optional] |
|**insuredForLife** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  |  [optional] |
|**interestRate** | [**Percent**](Percent.md) |  |  [optional] |
|**isInterestRateVariable** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  |  [optional] |
|**isPaymentVariable** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  |  [optional] |
|**linkedAssetId** | **String** |  |  [optional] [readonly] |
|**linkedAssetName** | **String** |  |  [optional] [readonly] |
|**loanDate** | [**Date**](Date.md) |  |  [optional] |
|**originalBalance** | [**Currency**](Currency.md) |  |  [optional] |
|**owner** | [**OwnerEnum**](#OwnerEnum) |  |  [optional] [readonly] |
|**paidOffByRetirement** | [**IOptionalFieldDescriptiveBoolean**](IOptionalFieldDescriptiveBoolean.md) |  |  [optional] |
|**payOffDate** | [**IOptionalFieldDate**](IOptionalFieldDate.md) |  |  [optional] |
|**payOffOptionType** | [**FormattedEnumTypePayOffOptionsType**](FormattedEnumTypePayOffOptionsType.md) |  |  [optional] |
|**paymentAmount** | [**IOptionalFieldCurrency**](IOptionalFieldCurrency.md) |  |  [optional] |
|**paymentFrequency** | [**FormattedEnumTypeFrequency**](FormattedEnumTypeFrequency.md) |  |  [optional] |
|**paymentType** | [**FormattedEnumTypePaymentType**](FormattedEnumTypePaymentType.md) |  |  [optional] |
|**type** | [**FormattedEnumTypeLiabilityType**](FormattedEnumTypeLiabilityType.md) |  |  [optional] |



## Enum: OwnerEnum

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |
| HEAD1 | &quot;Head1&quot; |
| HEAD2 | &quot;Head2&quot; |
| NON_HEAD1 | &quot;NonHead1&quot; |
| NON_HEAD2 | &quot;NonHead2&quot; |
| NON_HEAD3 | &quot;NonHead3&quot; |
| NON_HEAD4 | &quot;NonHead4&quot; |
| NON_HEAD5 | &quot;NonHead5&quot; |
| NON_HEAD6 | &quot;NonHead6&quot; |
| NON_HEAD7 | &quot;NonHead7&quot; |
| NON_HEAD8 | &quot;NonHead8&quot; |
| NON_HEAD9 | &quot;NonHead9&quot; |
| COMMUNITY_PROPERTY | &quot;CommunityProperty&quot; |
| JOINT | &quot;Joint&quot; |
| OTHER | &quot;Other&quot; |
| ALL_DEPENDENTS | &quot;AllDependents&quot; |
| ALL_FAMILY_MEMBERS | &quot;AllFamilyMembers&quot; |
| CORPORATION | &quot;Corporation&quot; |



