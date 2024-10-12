

# IPortfolioAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountReturnRatesNoLongerCorrelateToAssumedAssetMixDueToOverrideInGsm** | **Boolean** |  |  [optional] [readonly] |
|**annualFee** | [**Percent**](Percent.md) |  |  [optional] |
|**applicableRangeRetirementLiquidatedAssets** | [**FormattedDateRange**](FormattedDateRange.md) |  |  [optional] |
|**costBasis** | [**Currency**](Currency.md) |  |  [optional] |
|**description** | **String** |  |  [optional] [readonly] |
|**descriptionWithOwner** | **String** |  |  [optional] [readonly] |
|**excludeInAA** | **Boolean** |  |  [optional] [readonly] |
|**holdings** | [**List&lt;IHolding&gt;**](IHolding.md) |  |  [optional] [readonly] |
|**id** | **String** |  |  [optional] [readonly] |
|**isSystemGenerated** | **Boolean** |  |  [optional] [readonly] |
|**marketValue** | [**Currency**](Currency.md) |  |  [optional] |
|**owner** | [**OwnerEnum**](#OwnerEnum) |  |  [optional] [readonly] |
|**portfolioAssets** | [**List&lt;IPortfolioAsset&gt;**](IPortfolioAsset.md) |  |  [optional] [readonly] |
|**rateOfReturn** | [**IRateOfReturnDetails**](IRateOfReturnDetails.md) |  |  [optional] |
|**savingsStrategies** | [**ISavingsStrategies**](ISavingsStrategies.md) |  |  [optional] |
|**seppRedemptionStrategy** | [**ISEPPRedemptionStrategy**](ISEPPRedemptionStrategy.md) |  |  [optional] |
|**type** | **String** |  |  [optional] [readonly] |
|**valuationDate** | [**Date**](Date.md) |  |  [optional] |



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



