

# GuaranteedOrder

A guaranteed order. Guaranteed orders are parent entity of guaranteed inventory sources. When creating a guaranteed inventory source, a guaranteed order ID must be assigned to the inventory source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultAdvertiserId** | **String** | Output only. The ID of default advertiser of the guaranteed order. The default advertiser is either the read_write_advertiser_id or, if that is not set, the first advertiser listed in read_advertiser_ids. Otherwise, there is no default advertiser. |  [optional] [readonly] |
|**defaultCampaignId** | **String** | The ID of the default campaign that is assigned to the guaranteed order. The default campaign must belong to the default advertiser. |  [optional] |
|**displayName** | **String** | Required. The display name of the guaranteed order. Must be UTF-8 encoded with a maximum size of 240 bytes. |  [optional] |
|**exchange** | [**ExchangeEnum**](#ExchangeEnum) | Required. Immutable. The exchange where the guaranteed order originated. |  [optional] |
|**guaranteedOrderId** | **String** | Output only. The unique identifier of the guaranteed order. The guaranteed order IDs have the format &#x60;{exchange}-{legacy_guaranteed_order_id}&#x60;. |  [optional] [readonly] |
|**legacyGuaranteedOrderId** | **String** | Output only. The legacy ID of the guaranteed order. Assigned by the original exchange. The legacy ID is unique within one exchange, but is not guaranteed to be unique across all guaranteed orders. This ID is used in SDF and UI. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of the guaranteed order. |  [optional] [readonly] |
|**publisherName** | **String** | Required. The publisher name of the guaranteed order. Must be UTF-8 encoded with a maximum size of 240 bytes. |  [optional] |
|**readAccessInherited** | **Boolean** | Whether all advertisers of read_write_partner_id have read access to the guaranteed order. Only applicable if read_write_partner_id is set. If True, overrides read_advertiser_ids. |  [optional] |
|**readAdvertiserIds** | **List&lt;String&gt;** | The IDs of advertisers with read access to the guaranteed order. This field must not include the advertiser assigned to read_write_advertiser_id if it is set. All advertisers in this field must belong to read_write_partner_id or the same partner as read_write_advertiser_id. |  [optional] |
|**readWriteAdvertiserId** | **String** | The advertiser with read/write access to the guaranteed order. This is also the default advertiser of the guaranteed order. |  [optional] |
|**readWritePartnerId** | **String** | The partner with read/write access to the guaranteed order. |  [optional] |
|**status** | [**GuaranteedOrderStatus**](GuaranteedOrderStatus.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the guaranteed order was last updated. Assigned by the system. |  [optional] [readonly] |



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



