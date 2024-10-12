

# DealTerms

The deal terms specify the details of a Product/deal. They specify things like price per buyer, the type of pricing model (for example, fixed price, auction) and expected impressions from the publisher.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandingType** | [**BrandingTypeEnum**](#BrandingTypeEnum) | Visibility of the URL in bid requests. (default: BRANDED) |  [optional] |
|**description** | **String** | Publisher provided description for the terms. |  [optional] |
|**estimatedGrossSpend** | [**Price**](Price.md) |  |  [optional] |
|**estimatedImpressionsPerDay** | **String** | Non-binding estimate of the impressions served per day. Can be set by buyer or seller. |  [optional] |
|**guaranteedFixedPriceTerms** | [**GuaranteedFixedPriceTerms**](GuaranteedFixedPriceTerms.md) |  |  [optional] |
|**nonGuaranteedAuctionTerms** | [**NonGuaranteedAuctionTerms**](NonGuaranteedAuctionTerms.md) |  |  [optional] |
|**nonGuaranteedFixedPriceTerms** | [**NonGuaranteedFixedPriceTerms**](NonGuaranteedFixedPriceTerms.md) |  |  [optional] |
|**sellerTimeZone** | **String** | The time zone name. For deals with Cost Per Day billing, defines the time zone used to mark the boundaries of a day. It should be an IANA TZ name, such as \&quot;America/Los_Angeles\&quot;. For more information, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. |  [optional] |



## Enum: BrandingTypeEnum

| Name | Value |
|---- | -----|
| BRANDING_TYPE_UNSPECIFIED | &quot;BRANDING_TYPE_UNSPECIFIED&quot; |
| BRANDED | &quot;BRANDED&quot; |
| SEMI_TRANSPARENT | &quot;SEMI_TRANSPARENT&quot; |



