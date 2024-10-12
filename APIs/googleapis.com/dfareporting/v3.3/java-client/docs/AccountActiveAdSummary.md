

# AccountActiveAdSummary

Gets a summary of active ads in an account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | ID of the account. |  [optional] |
|**activeAds** | **String** | Ads that have been activated for the account |  [optional] |
|**activeAdsLimitTier** | [**ActiveAdsLimitTierEnum**](#ActiveAdsLimitTierEnum) | Maximum number of active ads allowed for the account. |  [optional] |
|**availableAds** | **String** | Ads that can be activated for the account. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#accountActiveAdSummary\&quot;. |  [optional] |



## Enum: ActiveAdsLimitTierEnum

| Name | Value |
|---- | -----|
| _40_K | &quot;ACTIVE_ADS_TIER_40K&quot; |
| _75_K | &quot;ACTIVE_ADS_TIER_75K&quot; |
| _100_K | &quot;ACTIVE_ADS_TIER_100K&quot; |
| _200_K | &quot;ACTIVE_ADS_TIER_200K&quot; |
| _300_K | &quot;ACTIVE_ADS_TIER_300K&quot; |
| _500_K | &quot;ACTIVE_ADS_TIER_500K&quot; |
| _750_K | &quot;ACTIVE_ADS_TIER_750K&quot; |
| _1_M | &quot;ACTIVE_ADS_TIER_1M&quot; |



