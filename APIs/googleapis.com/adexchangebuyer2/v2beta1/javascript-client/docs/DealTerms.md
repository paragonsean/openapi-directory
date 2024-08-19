# AdExchangeBuyerApiIi.DealTerms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brandingType** | **String** | Visibility of the URL in bid requests. (default: BRANDED) | [optional] 
**description** | **String** | Publisher provided description for the terms. | [optional] 
**estimatedGrossSpend** | [**Price**](Price.md) |  | [optional] 
**estimatedImpressionsPerDay** | **String** | Non-binding estimate of the impressions served per day. Can be set by buyer or seller. | [optional] 
**guaranteedFixedPriceTerms** | [**GuaranteedFixedPriceTerms**](GuaranteedFixedPriceTerms.md) |  | [optional] 
**nonGuaranteedAuctionTerms** | [**NonGuaranteedAuctionTerms**](NonGuaranteedAuctionTerms.md) |  | [optional] 
**nonGuaranteedFixedPriceTerms** | [**NonGuaranteedFixedPriceTerms**](NonGuaranteedFixedPriceTerms.md) |  | [optional] 
**sellerTimeZone** | **String** | The time zone name. For deals with Cost Per Day billing, defines the time zone used to mark the boundaries of a day. It should be an IANA TZ name, such as \&quot;America/Los_Angeles\&quot;. For more information, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. | [optional] 



## Enum: BrandingTypeEnum


* `BRANDING_TYPE_UNSPECIFIED` (value: `"BRANDING_TYPE_UNSPECIFIED"`)

* `BRANDED` (value: `"BRANDED"`)

* `SEMI_TRANSPARENT` (value: `"SEMI_TRANSPARENT"`)




