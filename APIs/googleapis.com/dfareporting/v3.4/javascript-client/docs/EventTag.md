# CampaignManager360Api.EventTag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of this event tag. This is a read-only field that can be left blank. | [optional] 
**advertiserId** | **String** | Advertiser ID of this event tag. This field or the campaignId field is required on insertion. | [optional] 
**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**campaignId** | **String** | Campaign ID of this event tag. This field or the advertiserId field is required on insertion. | [optional] 
**campaignIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**enabledByDefault** | **Boolean** | Whether this event tag should be automatically enabled for all of the advertiser&#39;s campaigns and ads. | [optional] 
**excludeFromAdxRequests** | **Boolean** | Whether to remove this event tag from ads that are trafficked through Display &amp; Video 360 to Ad Exchange. This may be useful if the event tag uses a pixel that is unapproved for Ad Exchange bids on one or more networks, such as the Google Display Network. | [optional] 
**id** | **String** | ID of this event tag. This is a read-only, auto-generated field. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#eventTag\&quot;. | [optional] 
**name** | **String** | Name of this event tag. This is a required field and must be less than 256 characters long. | [optional] 
**siteFilterType** | **String** | Site filter type for this event tag. If no type is specified then the event tag will be applied to all sites. | [optional] 
**siteIds** | **[String]** | Filter list of site IDs associated with this event tag. The siteFilterType determines whether this is a allowlist or blocklist filter. | [optional] 
**sslCompliant** | **Boolean** | Whether this tag is SSL-compliant or not. This is a read-only field. | [optional] 
**status** | **String** | Status of this event tag. Must be ENABLED for this event tag to fire. This is a required field. | [optional] 
**subaccountId** | **String** | Subaccount ID of this event tag. This is a read-only field that can be left blank. | [optional] 
**type** | **String** | Event tag type. Can be used to specify whether to use a third-party pixel, a third-party JavaScript URL, or a third-party click-through URL for either impression or click tracking. This is a required field. | [optional] 
**url** | **String** | Payload URL for this event tag. The URL on a click-through event tag should have a landing page URL appended to the end of it. This field is required on insertion. | [optional] 
**urlEscapeLevels** | **Number** | Number of times the landing page URL should be URL-escaped before being appended to the click-through event tag URL. Only applies to click-through event tags as specified by the event tag type. | [optional] 



## Enum: SiteFilterTypeEnum


* `WHITELIST` (value: `"WHITELIST"`)

* `BLACKLIST` (value: `"BLACKLIST"`)





## Enum: StatusEnum


* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)





## Enum: TypeEnum


* `IMPRESSION_IMAGE_EVENT_TAG` (value: `"IMPRESSION_IMAGE_EVENT_TAG"`)

* `IMPRESSION_JAVASCRIPT_EVENT_TAG` (value: `"IMPRESSION_JAVASCRIPT_EVENT_TAG"`)

* `CLICK_THROUGH_EVENT_TAG` (value: `"CLICK_THROUGH_EVENT_TAG"`)




