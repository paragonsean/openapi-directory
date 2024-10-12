

# RegionalPriceMigrationConfig

Configuration for a price migration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**oldestAllowedPriceVersionTime** | **String** | Required. The cutoff time for historical prices that subscribers can remain paying. Subscribers on prices which were available at this cutoff time or later will stay on their existing price. Subscribers on older prices will be migrated to the currently-offered price. The migrated subscribers will receive a notification that they will be paying a different price. Subscribers who do not agree to the new price will have their subscription ended at the next renewal. |  [optional] |
|**priceIncreaseType** | [**PriceIncreaseTypeEnum**](#PriceIncreaseTypeEnum) | Optional. The behavior the caller wants users to see when there is a price increase during migration. If left unset, the behavior defaults to PRICE_INCREASE_TYPE_OPT_IN. Note that the first opt-out price increase migration for each app must be initiated in Play Console. |  [optional] |
|**regionCode** | **String** | Required. Region code this configuration applies to, as defined by ISO 3166-2, e.g. \&quot;US\&quot;. |  [optional] |



## Enum: PriceIncreaseTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRICE_INCREASE_TYPE_UNSPECIFIED&quot; |
| OPT_IN | &quot;PRICE_INCREASE_TYPE_OPT_IN&quot; |
| OPT_OUT | &quot;PRICE_INCREASE_TYPE_OPT_OUT&quot; |



