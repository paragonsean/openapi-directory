

# IInsurancePremium


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**CurrencyWithGrowth**](CurrencyWithGrowth.md) |  |  [optional] |
|**annualAmount** | [**Currency**](Currency.md) |  |  [optional] |
|**ceaseDate** | [**Date**](Date.md) |  |  [optional] |
|**formattedPayingMember** | **String** |  |  [optional] [readonly] |
|**frequency** | [**IFormattedFrequency**](IFormattedFrequency.md) |  |  [optional] |
|**payingMember** | [**PayingMemberEnum**](#PayingMemberEnum) |  |  [optional] [readonly] |
|**premiumRefundAmount** | [**Percent**](Percent.md) |  |  [optional] |
|**startDate** | [**Date**](Date.md) |  |  [optional] |



## Enum: PayingMemberEnum

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



