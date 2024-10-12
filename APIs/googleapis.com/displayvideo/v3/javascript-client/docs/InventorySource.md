# DisplayVideo360Api.InventorySource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitment** | **String** | Whether the inventory source has a guaranteed or non-guaranteed delivery. | [optional] 
**creativeConfigs** | [**[CreativeConfig]**](CreativeConfig.md) | The creative requirements of the inventory source. Not applicable for auction packages. | [optional] 
**dealId** | **String** | The ID in the exchange space that uniquely identifies the inventory source. Must be unique across buyers within each exchange but not necessarily unique across exchanges. | [optional] 
**deliveryMethod** | **String** | The delivery method of the inventory source. * For non-guaranteed inventory sources, the only acceptable value is &#x60;INVENTORY_SOURCE_DELIVERY_METHOD_PROGRAMMATIC&#x60;. * For guaranteed inventory sources, acceptable values are &#x60;INVENTORY_SOURCE_DELIVERY_METHOD_TAG&#x60; and &#x60;INVENTORY_SOURCE_DELIVERY_METHOD_PROGRAMMATIC&#x60;. | [optional] 
**displayName** | **String** | The display name of the inventory source. Must be UTF-8 encoded with a maximum size of 240 bytes. | [optional] 
**exchange** | **String** | The exchange to which the inventory source belongs. | [optional] 
**guaranteedOrderId** | **String** | Immutable. The ID of the guaranteed order that this inventory source belongs to. Only applicable when commitment is &#x60;INVENTORY_SOURCE_COMMITMENT_GUARANTEED&#x60;. | [optional] 
**inventorySourceId** | **String** | Output only. The unique ID of the inventory source. Assigned by the system. | [optional] [readonly] 
**inventorySourceProductType** | **String** | Output only. The product type of the inventory source, denoting the way through which it sells inventory. | [optional] [readonly] 
**inventorySourceType** | **String** | Denotes the type of the inventory source. | [optional] 
**name** | **String** | Output only. The resource name of the inventory source. | [optional] [readonly] 
**publisherName** | **String** | The publisher/seller name of the inventory source. | [optional] 
**rateDetails** | [**RateDetails**](RateDetails.md) |  | [optional] 
**readAdvertiserIds** | **[String]** | Output only. The IDs of advertisers with read-only access to the inventory source. | [optional] [readonly] 
**readPartnerIds** | **[String]** | Output only. The IDs of partners with read-only access to the inventory source. All advertisers of partners in this field inherit read-only access to the inventory source. | [optional] [readonly] 
**readWriteAccessors** | [**InventorySourceAccessors**](InventorySourceAccessors.md) |  | [optional] 
**status** | [**InventorySourceStatus**](InventorySourceStatus.md) |  | [optional] 
**timeRange** | [**TimeRange**](TimeRange.md) |  | [optional] 
**updateTime** | **String** | Output only. The timestamp when the inventory source was last updated. Assigned by the system. | [optional] [readonly] 



## Enum: CommitmentEnum


* `UNSPECIFIED` (value: `"INVENTORY_SOURCE_COMMITMENT_UNSPECIFIED"`)

* `GUARANTEED` (value: `"INVENTORY_SOURCE_COMMITMENT_GUARANTEED"`)

* `NON_GUARANTEED` (value: `"INVENTORY_SOURCE_COMMITMENT_NON_GUARANTEED"`)





## Enum: DeliveryMethodEnum


* `UNSPECIFIED` (value: `"INVENTORY_SOURCE_DELIVERY_METHOD_UNSPECIFIED"`)

* `PROGRAMMATIC` (value: `"INVENTORY_SOURCE_DELIVERY_METHOD_PROGRAMMATIC"`)

* `TAG` (value: `"INVENTORY_SOURCE_DELIVERY_METHOD_TAG"`)





## Enum: ExchangeEnum


* `UNSPECIFIED` (value: `"EXCHANGE_UNSPECIFIED"`)

* `GOOGLE_AD_MANAGER` (value: `"EXCHANGE_GOOGLE_AD_MANAGER"`)

* `APPNEXUS` (value: `"EXCHANGE_APPNEXUS"`)

* `BRIGHTROLL` (value: `"EXCHANGE_BRIGHTROLL"`)

* `ADFORM` (value: `"EXCHANGE_ADFORM"`)

* `ADMETA` (value: `"EXCHANGE_ADMETA"`)

* `ADMIXER` (value: `"EXCHANGE_ADMIXER"`)

* `ADSMOGO` (value: `"EXCHANGE_ADSMOGO"`)

* `ADSWIZZ` (value: `"EXCHANGE_ADSWIZZ"`)

* `BIDSWITCH` (value: `"EXCHANGE_BIDSWITCH"`)

* `BRIGHTROLL_DISPLAY` (value: `"EXCHANGE_BRIGHTROLL_DISPLAY"`)

* `CADREON` (value: `"EXCHANGE_CADREON"`)

* `DAILYMOTION` (value: `"EXCHANGE_DAILYMOTION"`)

* `FIVE` (value: `"EXCHANGE_FIVE"`)

* `FLUCT` (value: `"EXCHANGE_FLUCT"`)

* `FREEWHEEL` (value: `"EXCHANGE_FREEWHEEL"`)

* `GENIEE` (value: `"EXCHANGE_GENIEE"`)

* `GUMGUM` (value: `"EXCHANGE_GUMGUM"`)

* `IMOBILE` (value: `"EXCHANGE_IMOBILE"`)

* `IBILLBOARD` (value: `"EXCHANGE_IBILLBOARD"`)

* `IMPROVE_DIGITAL` (value: `"EXCHANGE_IMPROVE_DIGITAL"`)

* `INDEX` (value: `"EXCHANGE_INDEX"`)

* `KARGO` (value: `"EXCHANGE_KARGO"`)

* `MICROAD` (value: `"EXCHANGE_MICROAD"`)

* `MOPUB` (value: `"EXCHANGE_MOPUB"`)

* `NEND` (value: `"EXCHANGE_NEND"`)

* `ONE_BY_AOL_DISPLAY` (value: `"EXCHANGE_ONE_BY_AOL_DISPLAY"`)

* `ONE_BY_AOL_MOBILE` (value: `"EXCHANGE_ONE_BY_AOL_MOBILE"`)

* `ONE_BY_AOL_VIDEO` (value: `"EXCHANGE_ONE_BY_AOL_VIDEO"`)

* `OOYALA` (value: `"EXCHANGE_OOYALA"`)

* `OPENX` (value: `"EXCHANGE_OPENX"`)

* `PERMODO` (value: `"EXCHANGE_PERMODO"`)

* `PLATFORMONE` (value: `"EXCHANGE_PLATFORMONE"`)

* `PLATFORMID` (value: `"EXCHANGE_PLATFORMID"`)

* `PUBMATIC` (value: `"EXCHANGE_PUBMATIC"`)

* `PULSEPOINT` (value: `"EXCHANGE_PULSEPOINT"`)

* `REVENUEMAX` (value: `"EXCHANGE_REVENUEMAX"`)

* `RUBICON` (value: `"EXCHANGE_RUBICON"`)

* `SMARTCLIP` (value: `"EXCHANGE_SMARTCLIP"`)

* `SMARTRTB` (value: `"EXCHANGE_SMARTRTB"`)

* `SMARTSTREAMTV` (value: `"EXCHANGE_SMARTSTREAMTV"`)

* `SOVRN` (value: `"EXCHANGE_SOVRN"`)

* `SPOTXCHANGE` (value: `"EXCHANGE_SPOTXCHANGE"`)

* `STROER` (value: `"EXCHANGE_STROER"`)

* `TEADSTV` (value: `"EXCHANGE_TEADSTV"`)

* `TELARIA` (value: `"EXCHANGE_TELARIA"`)

* `TVN` (value: `"EXCHANGE_TVN"`)

* `UNITED` (value: `"EXCHANGE_UNITED"`)

* `YIELDLAB` (value: `"EXCHANGE_YIELDLAB"`)

* `YIELDMO` (value: `"EXCHANGE_YIELDMO"`)

* `UNRULYX` (value: `"EXCHANGE_UNRULYX"`)

* `OPEN8` (value: `"EXCHANGE_OPEN8"`)

* `TRITON` (value: `"EXCHANGE_TRITON"`)

* `TRIPLELIFT` (value: `"EXCHANGE_TRIPLELIFT"`)

* `TABOOLA` (value: `"EXCHANGE_TABOOLA"`)

* `INMOBI` (value: `"EXCHANGE_INMOBI"`)

* `SMAATO` (value: `"EXCHANGE_SMAATO"`)

* `AJA` (value: `"EXCHANGE_AJA"`)

* `SUPERSHIP` (value: `"EXCHANGE_SUPERSHIP"`)

* `NEXSTAR_DIGITAL` (value: `"EXCHANGE_NEXSTAR_DIGITAL"`)

* `WAZE` (value: `"EXCHANGE_WAZE"`)

* `SOUNDCAST` (value: `"EXCHANGE_SOUNDCAST"`)

* `SHARETHROUGH` (value: `"EXCHANGE_SHARETHROUGH"`)

* `FYBER` (value: `"EXCHANGE_FYBER"`)

* `RED_FOR_PUBLISHERS` (value: `"EXCHANGE_RED_FOR_PUBLISHERS"`)

* `MEDIANET` (value: `"EXCHANGE_MEDIANET"`)

* `TAPJOY` (value: `"EXCHANGE_TAPJOY"`)

* `VISTAR` (value: `"EXCHANGE_VISTAR"`)

* `DAX` (value: `"EXCHANGE_DAX"`)

* `JCD` (value: `"EXCHANGE_JCD"`)

* `PLACE_EXCHANGE` (value: `"EXCHANGE_PLACE_EXCHANGE"`)

* `APPLOVIN` (value: `"EXCHANGE_APPLOVIN"`)

* `CONNATIX` (value: `"EXCHANGE_CONNATIX"`)

* `RESET_DIGITAL` (value: `"EXCHANGE_RESET_DIGITAL"`)

* `HIVESTACK` (value: `"EXCHANGE_HIVESTACK"`)

* `APPLOVIN_GBID` (value: `"EXCHANGE_APPLOVIN_GBID"`)

* `FYBER_GBID` (value: `"EXCHANGE_FYBER_GBID"`)

* `UNITY_GBID` (value: `"EXCHANGE_UNITY_GBID"`)

* `CHARTBOOST_GBID` (value: `"EXCHANGE_CHARTBOOST_GBID"`)

* `ADMOST_GBID` (value: `"EXCHANGE_ADMOST_GBID"`)

* `TOPON_GBID` (value: `"EXCHANGE_TOPON_GBID"`)





## Enum: InventorySourceProductTypeEnum


* `INVENTORY_SOURCE_PRODUCT_TYPE_UNSPECIFIED` (value: `"INVENTORY_SOURCE_PRODUCT_TYPE_UNSPECIFIED"`)

* `PREFERRED_DEAL` (value: `"PREFERRED_DEAL"`)

* `PRIVATE_AUCTION` (value: `"PRIVATE_AUCTION"`)

* `PROGRAMMATIC_GUARANTEED` (value: `"PROGRAMMATIC_GUARANTEED"`)

* `TAG_GUARANTEED` (value: `"TAG_GUARANTEED"`)

* `YOUTUBE_RESERVE` (value: `"YOUTUBE_RESERVE"`)

* `INSTANT_RESERVE` (value: `"INSTANT_RESERVE"`)

* `GUARANTEED_PACKAGE` (value: `"GUARANTEED_PACKAGE"`)

* `PROGRAMMATIC_TV` (value: `"PROGRAMMATIC_TV"`)

* `AUCTION_PACKAGE` (value: `"AUCTION_PACKAGE"`)





## Enum: InventorySourceTypeEnum


* `UNSPECIFIED` (value: `"INVENTORY_SOURCE_TYPE_UNSPECIFIED"`)

* `PRIVATE` (value: `"INVENTORY_SOURCE_TYPE_PRIVATE"`)

* `AUCTION_PACKAGE` (value: `"INVENTORY_SOURCE_TYPE_AUCTION_PACKAGE"`)




