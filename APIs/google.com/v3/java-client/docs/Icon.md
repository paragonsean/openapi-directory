

# Icon

Information about a partner's icon.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disapprovalReasons** | [**List&lt;DisapprovalReasonsEnum&gt;**](#List&lt;DisapprovalReasonsEnum&gt;) | Output only. The icon&#39;s disapproval reason(s). Only applies to icons with &#x60;REJECTED&#x60; state. |  [optional] [readonly] |
|**iconUri** | **String** | Output only. The approved icon&#39;s Google-hosted URI. Only applies to icons with &#x60;APPROVED&#x60; state. |  [optional] [readonly] |
|**imageData** | **byte[]** | Required. Input only. The icon contents, which must be in PNG format, or convertible to PNG. |  [optional] |
|**name** | **String** | Required. Output only. The resource name for the icon in the format &#x60;accounts/{account_id}/icons/{icon_id}&#x60;. Google generates the &#x60;icon_id&#x60; during the &#x60;create&#x60; operation. Use the &#x60;icon_id&#x60; to associate the icon with a brand using the [accounts.brands](/hotels/hotel-prices/api-reference/rest/v3/accounts.brands#resource:-brand) API. |  [optional] [readonly] |
|**reference** | **String** | Optional. Value for tracking the icon. It could be the primary key to your icon in your system, or the icon&#39;s filename. Google does not use this value. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The icon&#39;s current state. |  [optional] [readonly] |



## Enum: List&lt;DisapprovalReasonsEnum&gt;

| Name | Value |
|---- | -----|
| IMAGE_DISAPPROVAL_REASON_UNSPECIFIED | &quot;IMAGE_DISAPPROVAL_REASON_UNSPECIFIED&quot; |
| NOT_LIKE_SITE | &quot;NOT_LIKE_SITE&quot; |
| OFFENSIVE | &quot;OFFENSIVE&quot; |
| LOW_QUALITY | &quot;LOW_QUALITY&quot; |
| ANIMATED | &quot;ANIMATED&quot; |
| BAD_BACKGROUND | &quot;BAD_BACKGROUND&quot; |
| TEXT_TOO_SMALL | &quot;TEXT_TOO_SMALL&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| NEW | &quot;NEW&quot; |
| APPROVED | &quot;APPROVED&quot; |
| REJECTED | &quot;REJECTED&quot; |



