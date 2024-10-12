# NaviPlanApi.IPortfolioAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountReturnRatesNoLongerCorrelateToAssumedAssetMixDueToOverrideInGsm** | **Boolean** |  | [optional] [readonly] 
**annualFee** | [**Percent**](Percent.md) |  | [optional] 
**applicableRangeRetirementLiquidatedAssets** | [**FormattedDateRange**](FormattedDateRange.md) |  | [optional] 
**costBasis** | [**Currency**](Currency.md) |  | [optional] 
**description** | **String** |  | [optional] [readonly] 
**descriptionWithOwner** | **String** |  | [optional] [readonly] 
**excludeInAA** | **Boolean** |  | [optional] [readonly] 
**holdings** | [**[IHolding]**](IHolding.md) |  | [optional] [readonly] 
**id** | **String** |  | [optional] [readonly] 
**isSystemGenerated** | **Boolean** |  | [optional] [readonly] 
**marketValue** | [**Currency**](Currency.md) |  | [optional] 
**owner** | **String** |  | [optional] [readonly] 
**portfolioAssets** | [**[IPortfolioAsset]**](IPortfolioAsset.md) |  | [optional] [readonly] 
**rateOfReturn** | [**IRateOfReturnDetails**](IRateOfReturnDetails.md) |  | [optional] 
**savingsStrategies** | [**ISavingsStrategies**](ISavingsStrategies.md) |  | [optional] 
**seppRedemptionStrategy** | [**ISEPPRedemptionStrategy**](ISEPPRedemptionStrategy.md) |  | [optional] 
**type** | **String** |  | [optional] [readonly] 
**valuationDate** | [**ModelDate**](ModelDate.md) |  | [optional] 



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




