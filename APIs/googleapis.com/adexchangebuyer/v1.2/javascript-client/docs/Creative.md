# AdExchangeBuyerApi.Creative

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hTMLSnippet** | **String** | The HTML snippet that displays the ad when inserted in the web page. If set, videoURL should not be set. | [optional] 
**accountId** | **Number** | Account id. | [optional] 
**advertiserId** | **[String]** | Detected advertiser id, if any. Read-only. This field should not be set in requests. | [optional] 
**advertiserName** | **String** | The name of the company being advertised in the creative. | [optional] 
**agencyId** | **String** | The agency id for this creative. | [optional] 
**apiUploadTimestamp** | **Date** | The last upload timestamp of this creative if it was uploaded via API. Read-only. The value of this field is generated, and will be ignored for uploads. (formatted RFC 3339 timestamp). | [optional] 
**attribute** | **[Number]** | All attributes for the ads that may be shown from this snippet. | [optional] 
**buyerCreativeId** | **String** | A buyer-specific id identifying the creative in this ad. | [optional] 
**clickThroughUrl** | **[String]** | The set of destination urls for the snippet. | [optional] 
**corrections** | [**[CreativeCorrectionsInner]**](CreativeCorrectionsInner.md) | Shows any corrections that were applied to this creative. Read-only. This field should not be set in requests. | [optional] 
**disapprovalReasons** | [**[CreativeDisapprovalReasonsInner]**](CreativeDisapprovalReasonsInner.md) | The reasons for disapproval, if any. Note that not all disapproval reasons may be categorized, so it is possible for the creative to have a status of DISAPPROVED with an empty list for disapproval_reasons. In this case, please reach out to your TAM to help debug the issue. Read-only. This field should not be set in requests. | [optional] 
**filteringReasons** | [**CreativeFilteringReasons**](CreativeFilteringReasons.md) |  | [optional] 
**height** | **Number** | Ad height. | [optional] 
**impressionTrackingUrl** | **[String]** | The set of urls to be called to record an impression. | [optional] 
**kind** | **String** | Resource type. | [optional] [default to &#39;adexchangebuyer#creative&#39;]
**productCategories** | **[Number]** | Detected product categories, if any. Read-only. This field should not be set in requests. | [optional] 
**restrictedCategories** | **[Number]** | All restricted categories for the ads that may be shown from this snippet. | [optional] 
**sensitiveCategories** | **[Number]** | Detected sensitive categories, if any. Read-only. This field should not be set in requests. | [optional] 
**status** | **String** | Creative serving status. Read-only. This field should not be set in requests. | [optional] 
**vendorType** | **[Number]** | All vendor types for the ads that may be shown from this snippet. | [optional] 
**version** | **Number** | The version for this creative. Read-only. This field should not be set in requests. | [optional] 
**videoURL** | **String** | The url to fetch a video ad. If set, HTMLSnippet should not be set. | [optional] 
**width** | **Number** | Ad width. | [optional] 


