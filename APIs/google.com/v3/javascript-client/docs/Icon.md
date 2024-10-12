# TravelPartnerApi.Icon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disapprovalReasons** | **[String]** | Output only. The icon&#39;s disapproval reason(s). Only applies to icons with &#x60;REJECTED&#x60; state. | [optional] [readonly] 
**iconUri** | **String** | Output only. The approved icon&#39;s Google-hosted URI. Only applies to icons with &#x60;APPROVED&#x60; state. | [optional] [readonly] 
**imageData** | **Blob** | Required. Input only. The icon contents, which must be in PNG format, or convertible to PNG. | [optional] 
**name** | **String** | Required. Output only. The resource name for the icon in the format &#x60;accounts/{account_id}/icons/{icon_id}&#x60;. Google generates the &#x60;icon_id&#x60; during the &#x60;create&#x60; operation. Use the &#x60;icon_id&#x60; to associate the icon with a brand using the [accounts.brands](/hotels/hotel-prices/api-reference/rest/v3/accounts.brands#resource:-brand) API. | [optional] [readonly] 
**reference** | **String** | Optional. Value for tracking the icon. It could be the primary key to your icon in your system, or the icon&#39;s filename. Google does not use this value. | [optional] 
**state** | **String** | Output only. The icon&#39;s current state. | [optional] [readonly] 



## Enum: [DisapprovalReasonsEnum]


* `IMAGE_DISAPPROVAL_REASON_UNSPECIFIED` (value: `"IMAGE_DISAPPROVAL_REASON_UNSPECIFIED"`)

* `NOT_LIKE_SITE` (value: `"NOT_LIKE_SITE"`)

* `OFFENSIVE` (value: `"OFFENSIVE"`)

* `LOW_QUALITY` (value: `"LOW_QUALITY"`)

* `ANIMATED` (value: `"ANIMATED"`)

* `BAD_BACKGROUND` (value: `"BAD_BACKGROUND"`)

* `TEXT_TOO_SMALL` (value: `"TEXT_TOO_SMALL"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `NEW` (value: `"NEW"`)

* `APPROVED` (value: `"APPROVED"`)

* `REJECTED` (value: `"REJECTED"`)




