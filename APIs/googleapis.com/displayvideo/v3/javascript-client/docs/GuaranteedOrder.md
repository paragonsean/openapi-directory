# DisplayVideo360Api.GuaranteedOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultAdvertiserId** | **String** | Output only. The ID of default advertiser of the guaranteed order. The default advertiser is either the read_write_advertiser_id or, if that is not set, the first advertiser listed in read_advertiser_ids. Otherwise, there is no default advertiser. | [optional] [readonly] 
**defaultCampaignId** | **String** | The ID of the default campaign that is assigned to the guaranteed order. The default campaign must belong to the default advertiser. | [optional] 
**displayName** | **String** | Required. The display name of the guaranteed order. Must be UTF-8 encoded with a maximum size of 240 bytes. | [optional] 
**exchange** | **String** | Required. Immutable. The exchange where the guaranteed order originated. | [optional] 
**guaranteedOrderId** | **String** | Output only. The unique identifier of the guaranteed order. The guaranteed order IDs have the format &#x60;{exchange}-{legacy_guaranteed_order_id}&#x60;. | [optional] [readonly] 
**legacyGuaranteedOrderId** | **String** | Output only. The legacy ID of the guaranteed order. Assigned by the original exchange. The legacy ID is unique within one exchange, but is not guaranteed to be unique across all guaranteed orders. This ID is used in SDF and UI. | [optional] [readonly] 
**name** | **String** | Output only. The resource name of the guaranteed order. | [optional] [readonly] 
**publisherName** | **String** | Required. The publisher name of the guaranteed order. Must be UTF-8 encoded with a maximum size of 240 bytes. | [optional] 
**readAccessInherited** | **Boolean** | Whether all advertisers of read_write_partner_id have read access to the guaranteed order. Only applicable if read_write_partner_id is set. If True, overrides read_advertiser_ids. | [optional] 
**readAdvertiserIds** | **[String]** | The IDs of advertisers with read access to the guaranteed order. This field must not include the advertiser assigned to read_write_advertiser_id if it is set. All advertisers in this field must belong to read_write_partner_id or the same partner as read_write_advertiser_id. | [optional] 
**readWriteAdvertiserId** | **String** | The advertiser with read/write access to the guaranteed order. This is also the default advertiser of the guaranteed order. | [optional] 
**readWritePartnerId** | **String** | The partner with read/write access to the guaranteed order. | [optional] 
**status** | [**GuaranteedOrderStatus**](GuaranteedOrderStatus.md) |  | [optional] 
**updateTime** | **String** | Output only. The timestamp when the guaranteed order was last updated. Assigned by the system. | [optional] [readonly] 



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




