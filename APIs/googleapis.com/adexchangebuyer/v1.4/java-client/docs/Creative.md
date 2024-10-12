

# Creative

A creative and its classification data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**htMLSnippet** | **String** | The HTML snippet that displays the ad when inserted in the web page. If set, videoURL, videoVastXML, and nativeAd should not be set. |  [optional] |
|**accountId** | **Integer** | Account id. |  [optional] |
|**adChoicesDestinationUrl** | **String** | The link to the Ad Preferences page. This is only supported for native ads. |  [optional] |
|**adTechnologyProviders** | [**CreativeAdTechnologyProviders**](CreativeAdTechnologyProviders.md) |  |  [optional] |
|**advertiserId** | **List&lt;String&gt;** | Detected advertiser id, if any. Read-only. This field should not be set in requests. |  [optional] |
|**advertiserName** | **String** | The name of the company being advertised in the creative. A list of advertisers is provided in the advertisers.txt file. |  [optional] |
|**agencyId** | **String** | The agency id for this creative. |  [optional] |
|**apiUploadTimestamp** | **OffsetDateTime** | The last upload timestamp of this creative if it was uploaded via API. Read-only. The value of this field is generated, and will be ignored for uploads. (formatted RFC 3339 timestamp). |  [optional] |
|**attribute** | **List&lt;Integer&gt;** | List of buyer selectable attributes for the ads that may be shown from this snippet. Each attribute is represented by an integer as defined in  buyer-declarable-creative-attributes.txt. |  [optional] |
|**buyerCreativeId** | **String** | A buyer-specific id identifying the creative in this ad. |  [optional] |
|**clickThroughUrl** | **List&lt;String&gt;** | The set of destination urls for the snippet. |  [optional] |
|**corrections** | [**List&lt;CreativeCorrectionsInner&gt;**](CreativeCorrectionsInner.md) | Shows any corrections that were applied to this creative. Read-only. This field should not be set in requests. |  [optional] |
|**creativeStatusIdentityType** | **String** | Creative status identity type that the creative item applies to. Ad Exchange real-time bidding is migrating to the sizeless creative verification. Originally, Ad Exchange assigned creative verification status to a unique combination of a buyer creative ID and creative dimensions. Post-migration, a single verification status will be assigned at the buyer creative ID level. This field allows to distinguish whether a given creative status applies to a unique combination of a buyer creative ID and creative dimensions, or to a buyer creative ID as a whole. |  [optional] |
|**dealsStatus** | **String** | Top-level deals status. Read-only. This field should not be set in requests. If disapproved, an entry for auctionType&#x3D;DIRECT_DEALS (or ALL) in servingRestrictions will also exist. Note that this may be nuanced with other contextual restrictions, in which case it may be preferable to read from servingRestrictions directly. |  [optional] |
|**detectedDomains** | **List&lt;String&gt;** | Detected domains for this creative. Read-only. This field should not be set in requests. |  [optional] |
|**filteringReasons** | [**CreativeFilteringReasons**](CreativeFilteringReasons.md) |  |  [optional] |
|**height** | **Integer** | Ad height. |  [optional] |
|**impressionTrackingUrl** | **List&lt;String&gt;** | The set of urls to be called to record an impression. |  [optional] |
|**kind** | **String** | Resource type. |  [optional] |
|**languages** | **List&lt;String&gt;** | Detected languages for this creative. Read-only. This field should not be set in requests. |  [optional] |
|**nativeAd** | [**CreativeNativeAd**](CreativeNativeAd.md) |  |  [optional] |
|**openAuctionStatus** | **String** | Top-level open auction status. Read-only. This field should not be set in requests. If disapproved, an entry for auctionType&#x3D;OPEN_AUCTION (or ALL) in servingRestrictions will also exist. Note that this may be nuanced with other contextual restrictions, in which case it may be preferable to read from ServingRestrictions directly. |  [optional] |
|**productCategories** | **List&lt;Integer&gt;** | Detected product categories, if any. Each category is represented by an integer as defined in  ad-product-categories.txt. Read-only. This field should not be set in requests. |  [optional] |
|**restrictedCategories** | **List&lt;Integer&gt;** | All restricted categories for the ads that may be shown from this snippet. Each category is represented by an integer as defined in the  ad-restricted-categories.txt. |  [optional] |
|**sensitiveCategories** | **List&lt;Integer&gt;** | Detected sensitive categories, if any. Each category is represented by an integer as defined in  ad-sensitive-categories.txt. Read-only. This field should not be set in requests. |  [optional] |
|**servingRestrictions** | [**List&lt;CreativeServingRestrictionsInner&gt;**](CreativeServingRestrictionsInner.md) | The granular status of this ad in specific contexts. A context here relates to where something ultimately serves (for example, a physical location, a platform, an HTTPS vs HTTP request, or the type of auction). Read-only. This field should not be set in requests. See the examples in the Creatives guide for more details. |  [optional] |
|**vendorType** | **List&lt;Integer&gt;** | List of vendor types for the ads that may be shown from this snippet. Each vendor type is represented by an integer as defined in vendors.txt. |  [optional] |
|**version** | **Integer** | The version for this creative. Read-only. This field should not be set in requests. |  [optional] |
|**videoURL** | **String** | The URL to fetch a video ad. If set, HTMLSnippet, videoVastXML, and nativeAd should not be set. Note, this is different from resource.native_ad.video_url above. |  [optional] |
|**videoVastXML** | **String** | The contents of a VAST document for a video ad. This document should conform to the VAST 2.0 or 3.0 standard. If set, HTMLSnippet, videoURL, and nativeAd and should not be set. |  [optional] |
|**width** | **Integer** | Ad width. |  [optional] |



