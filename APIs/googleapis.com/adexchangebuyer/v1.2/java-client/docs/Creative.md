

# Creative

A creative and its classification data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**htMLSnippet** | **String** | The HTML snippet that displays the ad when inserted in the web page. If set, videoURL should not be set. |  [optional] |
|**accountId** | **Integer** | Account id. |  [optional] |
|**advertiserId** | **List&lt;String&gt;** | Detected advertiser id, if any. Read-only. This field should not be set in requests. |  [optional] |
|**advertiserName** | **String** | The name of the company being advertised in the creative. |  [optional] |
|**agencyId** | **String** | The agency id for this creative. |  [optional] |
|**apiUploadTimestamp** | **OffsetDateTime** | The last upload timestamp of this creative if it was uploaded via API. Read-only. The value of this field is generated, and will be ignored for uploads. (formatted RFC 3339 timestamp). |  [optional] |
|**attribute** | **List&lt;Integer&gt;** | All attributes for the ads that may be shown from this snippet. |  [optional] |
|**buyerCreativeId** | **String** | A buyer-specific id identifying the creative in this ad. |  [optional] |
|**clickThroughUrl** | **List&lt;String&gt;** | The set of destination urls for the snippet. |  [optional] |
|**corrections** | [**List&lt;CreativeCorrectionsInner&gt;**](CreativeCorrectionsInner.md) | Shows any corrections that were applied to this creative. Read-only. This field should not be set in requests. |  [optional] |
|**disapprovalReasons** | [**List&lt;CreativeDisapprovalReasonsInner&gt;**](CreativeDisapprovalReasonsInner.md) | The reasons for disapproval, if any. Note that not all disapproval reasons may be categorized, so it is possible for the creative to have a status of DISAPPROVED with an empty list for disapproval_reasons. In this case, please reach out to your TAM to help debug the issue. Read-only. This field should not be set in requests. |  [optional] |
|**filteringReasons** | [**CreativeFilteringReasons**](CreativeFilteringReasons.md) |  |  [optional] |
|**height** | **Integer** | Ad height. |  [optional] |
|**impressionTrackingUrl** | **List&lt;String&gt;** | The set of urls to be called to record an impression. |  [optional] |
|**kind** | **String** | Resource type. |  [optional] |
|**productCategories** | **List&lt;Integer&gt;** | Detected product categories, if any. Read-only. This field should not be set in requests. |  [optional] |
|**restrictedCategories** | **List&lt;Integer&gt;** | All restricted categories for the ads that may be shown from this snippet. |  [optional] |
|**sensitiveCategories** | **List&lt;Integer&gt;** | Detected sensitive categories, if any. Read-only. This field should not be set in requests. |  [optional] |
|**status** | **String** | Creative serving status. Read-only. This field should not be set in requests. |  [optional] |
|**vendorType** | **List&lt;Integer&gt;** | All vendor types for the ads that may be shown from this snippet. |  [optional] |
|**version** | **Integer** | The version for this creative. Read-only. This field should not be set in requests. |  [optional] |
|**videoURL** | **String** | The url to fetch a video ad. If set, HTMLSnippet should not be set. |  [optional] |
|**width** | **Integer** | Ad width. |  [optional] |



