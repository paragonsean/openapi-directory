

# InventorySource

An inventory source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitment** | [**CommitmentEnum**](#CommitmentEnum) | Whether the inventory source has a guaranteed or non-guaranteed delivery. |  [optional] |
|**creativeConfigs** | [**List&lt;CreativeConfig&gt;**](CreativeConfig.md) | The creative requirements of the inventory source. Not applicable for auction packages. |  [optional] |
|**dealId** | **String** | The ID in the exchange space that uniquely identifies the inventory source. Must be unique across buyers within each exchange but not necessarily unique across exchanges. |  [optional] |
|**deliveryMethod** | [**DeliveryMethodEnum**](#DeliveryMethodEnum) | The delivery method of the inventory source. * For non-guaranteed inventory sources, the only acceptable value is &#x60;INVENTORY_SOURCE_DELIVERY_METHOD_PROGRAMMATIC&#x60;. * For guaranteed inventory sources, acceptable values are &#x60;INVENTORY_SOURCE_DELIVERY_METHOD_TAG&#x60; and &#x60;INVENTORY_SOURCE_DELIVERY_METHOD_PROGRAMMATIC&#x60;. |  [optional] |
|**displayName** | **String** | The display name of the inventory source. Must be UTF-8 encoded with a maximum size of 240 bytes. |  [optional] |
|**exchange** | [**ExchangeEnum**](#ExchangeEnum) | The exchange to which the inventory source belongs. |  [optional] |
|**guaranteedOrderId** | **String** | Immutable. The ID of the guaranteed order that this inventory source belongs to. Only applicable when commitment is &#x60;INVENTORY_SOURCE_COMMITMENT_GUARANTEED&#x60;. |  [optional] |
|**inventorySourceId** | **String** | Output only. The unique ID of the inventory source. Assigned by the system. |  [optional] [readonly] |
|**inventorySourceProductType** | [**InventorySourceProductTypeEnum**](#InventorySourceProductTypeEnum) | Output only. The product type of the inventory source, denoting the way through which it sells inventory. |  [optional] [readonly] |
|**inventorySourceType** | [**InventorySourceTypeEnum**](#InventorySourceTypeEnum) | Denotes the type of the inventory source. |  [optional] |
|**name** | **String** | Output only. The resource name of the inventory source. |  [optional] [readonly] |
|**publisherName** | **String** | The publisher/seller name of the inventory source. |  [optional] |
|**rateDetails** | [**RateDetails**](RateDetails.md) |  |  [optional] |
|**readAdvertiserIds** | **List&lt;String&gt;** | Output only. The IDs of advertisers with read-only access to the inventory source. |  [optional] [readonly] |
|**readPartnerIds** | **List&lt;String&gt;** | Output only. The IDs of partners with read-only access to the inventory source. All advertisers of partners in this field inherit read-only access to the inventory source. |  [optional] [readonly] |
|**readWriteAccessors** | [**InventorySourceAccessors**](InventorySourceAccessors.md) |  |  [optional] |
|**status** | [**InventorySourceStatus**](InventorySourceStatus.md) |  |  [optional] |
|**timeRange** | [**TimeRange**](TimeRange.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the inventory source was last updated. Assigned by the system. |  [optional] [readonly] |



## Enum: CommitmentEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INVENTORY_SOURCE_COMMITMENT_UNSPECIFIED&quot; |
| GUARANTEED | &quot;INVENTORY_SOURCE_COMMITMENT_GUARANTEED&quot; |
| NON_GUARANTEED | &quot;INVENTORY_SOURCE_COMMITMENT_NON_GUARANTEED&quot; |



## Enum: DeliveryMethodEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INVENTORY_SOURCE_DELIVERY_METHOD_UNSPECIFIED&quot; |
| PROGRAMMATIC | &quot;INVENTORY_SOURCE_DELIVERY_METHOD_PROGRAMMATIC&quot; |
| TAG | &quot;INVENTORY_SOURCE_DELIVERY_METHOD_TAG&quot; |



## Enum: ExchangeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;EXCHANGE_UNSPECIFIED&quot; |
| GOOGLE_AD_MANAGER | &quot;EXCHANGE_GOOGLE_AD_MANAGER&quot; |
| APPNEXUS | &quot;EXCHANGE_APPNEXUS&quot; |
| BRIGHTROLL | &quot;EXCHANGE_BRIGHTROLL&quot; |
| ADFORM | &quot;EXCHANGE_ADFORM&quot; |
| ADMETA | &quot;EXCHANGE_ADMETA&quot; |
| ADMIXER | &quot;EXCHANGE_ADMIXER&quot; |
| ADSMOGO | &quot;EXCHANGE_ADSMOGO&quot; |
| ADSWIZZ | &quot;EXCHANGE_ADSWIZZ&quot; |
| BIDSWITCH | &quot;EXCHANGE_BIDSWITCH&quot; |
| BRIGHTROLL_DISPLAY | &quot;EXCHANGE_BRIGHTROLL_DISPLAY&quot; |
| CADREON | &quot;EXCHANGE_CADREON&quot; |
| DAILYMOTION | &quot;EXCHANGE_DAILYMOTION&quot; |
| FIVE | &quot;EXCHANGE_FIVE&quot; |
| FLUCT | &quot;EXCHANGE_FLUCT&quot; |
| FREEWHEEL | &quot;EXCHANGE_FREEWHEEL&quot; |
| GENIEE | &quot;EXCHANGE_GENIEE&quot; |
| GUMGUM | &quot;EXCHANGE_GUMGUM&quot; |
| IMOBILE | &quot;EXCHANGE_IMOBILE&quot; |
| IBILLBOARD | &quot;EXCHANGE_IBILLBOARD&quot; |
| IMPROVE_DIGITAL | &quot;EXCHANGE_IMPROVE_DIGITAL&quot; |
| INDEX | &quot;EXCHANGE_INDEX&quot; |
| KARGO | &quot;EXCHANGE_KARGO&quot; |
| MICROAD | &quot;EXCHANGE_MICROAD&quot; |
| MOPUB | &quot;EXCHANGE_MOPUB&quot; |
| NEND | &quot;EXCHANGE_NEND&quot; |
| ONE_BY_AOL_DISPLAY | &quot;EXCHANGE_ONE_BY_AOL_DISPLAY&quot; |
| ONE_BY_AOL_MOBILE | &quot;EXCHANGE_ONE_BY_AOL_MOBILE&quot; |
| ONE_BY_AOL_VIDEO | &quot;EXCHANGE_ONE_BY_AOL_VIDEO&quot; |
| OOYALA | &quot;EXCHANGE_OOYALA&quot; |
| OPENX | &quot;EXCHANGE_OPENX&quot; |
| PERMODO | &quot;EXCHANGE_PERMODO&quot; |
| PLATFORMONE | &quot;EXCHANGE_PLATFORMONE&quot; |
| PLATFORMID | &quot;EXCHANGE_PLATFORMID&quot; |
| PUBMATIC | &quot;EXCHANGE_PUBMATIC&quot; |
| PULSEPOINT | &quot;EXCHANGE_PULSEPOINT&quot; |
| REVENUEMAX | &quot;EXCHANGE_REVENUEMAX&quot; |
| RUBICON | &quot;EXCHANGE_RUBICON&quot; |
| SMARTCLIP | &quot;EXCHANGE_SMARTCLIP&quot; |
| SMARTRTB | &quot;EXCHANGE_SMARTRTB&quot; |
| SMARTSTREAMTV | &quot;EXCHANGE_SMARTSTREAMTV&quot; |
| SOVRN | &quot;EXCHANGE_SOVRN&quot; |
| SPOTXCHANGE | &quot;EXCHANGE_SPOTXCHANGE&quot; |
| STROER | &quot;EXCHANGE_STROER&quot; |
| TEADSTV | &quot;EXCHANGE_TEADSTV&quot; |
| TELARIA | &quot;EXCHANGE_TELARIA&quot; |
| TVN | &quot;EXCHANGE_TVN&quot; |
| UNITED | &quot;EXCHANGE_UNITED&quot; |
| YIELDLAB | &quot;EXCHANGE_YIELDLAB&quot; |
| YIELDMO | &quot;EXCHANGE_YIELDMO&quot; |
| UNRULYX | &quot;EXCHANGE_UNRULYX&quot; |
| OPEN8 | &quot;EXCHANGE_OPEN8&quot; |
| TRITON | &quot;EXCHANGE_TRITON&quot; |
| TRIPLELIFT | &quot;EXCHANGE_TRIPLELIFT&quot; |
| TABOOLA | &quot;EXCHANGE_TABOOLA&quot; |
| INMOBI | &quot;EXCHANGE_INMOBI&quot; |
| SMAATO | &quot;EXCHANGE_SMAATO&quot; |
| AJA | &quot;EXCHANGE_AJA&quot; |
| SUPERSHIP | &quot;EXCHANGE_SUPERSHIP&quot; |
| NEXSTAR_DIGITAL | &quot;EXCHANGE_NEXSTAR_DIGITAL&quot; |
| WAZE | &quot;EXCHANGE_WAZE&quot; |
| SOUNDCAST | &quot;EXCHANGE_SOUNDCAST&quot; |
| SHARETHROUGH | &quot;EXCHANGE_SHARETHROUGH&quot; |
| FYBER | &quot;EXCHANGE_FYBER&quot; |
| RED_FOR_PUBLISHERS | &quot;EXCHANGE_RED_FOR_PUBLISHERS&quot; |
| MEDIANET | &quot;EXCHANGE_MEDIANET&quot; |
| TAPJOY | &quot;EXCHANGE_TAPJOY&quot; |
| VISTAR | &quot;EXCHANGE_VISTAR&quot; |
| DAX | &quot;EXCHANGE_DAX&quot; |
| JCD | &quot;EXCHANGE_JCD&quot; |
| PLACE_EXCHANGE | &quot;EXCHANGE_PLACE_EXCHANGE&quot; |
| APPLOVIN | &quot;EXCHANGE_APPLOVIN&quot; |
| CONNATIX | &quot;EXCHANGE_CONNATIX&quot; |
| RESET_DIGITAL | &quot;EXCHANGE_RESET_DIGITAL&quot; |
| HIVESTACK | &quot;EXCHANGE_HIVESTACK&quot; |
| APPLOVIN_GBID | &quot;EXCHANGE_APPLOVIN_GBID&quot; |
| FYBER_GBID | &quot;EXCHANGE_FYBER_GBID&quot; |
| UNITY_GBID | &quot;EXCHANGE_UNITY_GBID&quot; |
| CHARTBOOST_GBID | &quot;EXCHANGE_CHARTBOOST_GBID&quot; |
| ADMOST_GBID | &quot;EXCHANGE_ADMOST_GBID&quot; |
| TOPON_GBID | &quot;EXCHANGE_TOPON_GBID&quot; |



## Enum: InventorySourceProductTypeEnum

| Name | Value |
|---- | -----|
| INVENTORY_SOURCE_PRODUCT_TYPE_UNSPECIFIED | &quot;INVENTORY_SOURCE_PRODUCT_TYPE_UNSPECIFIED&quot; |
| PREFERRED_DEAL | &quot;PREFERRED_DEAL&quot; |
| PRIVATE_AUCTION | &quot;PRIVATE_AUCTION&quot; |
| PROGRAMMATIC_GUARANTEED | &quot;PROGRAMMATIC_GUARANTEED&quot; |
| TAG_GUARANTEED | &quot;TAG_GUARANTEED&quot; |
| YOUTUBE_RESERVE | &quot;YOUTUBE_RESERVE&quot; |
| INSTANT_RESERVE | &quot;INSTANT_RESERVE&quot; |
| GUARANTEED_PACKAGE | &quot;GUARANTEED_PACKAGE&quot; |
| PROGRAMMATIC_TV | &quot;PROGRAMMATIC_TV&quot; |
| AUCTION_PACKAGE | &quot;AUCTION_PACKAGE&quot; |



## Enum: InventorySourceTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INVENTORY_SOURCE_TYPE_UNSPECIFIED&quot; |
| PRIVATE | &quot;INVENTORY_SOURCE_TYPE_PRIVATE&quot; |
| AUCTION_PACKAGE | &quot;INVENTORY_SOURCE_TYPE_AUCTION_PACKAGE&quot; |



