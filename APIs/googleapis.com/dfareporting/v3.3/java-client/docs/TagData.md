

# TagData

Placement Tag Data

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adId** | **String** | Ad associated with this placement tag. Applicable only when format is PLACEMENT_TAG_TRACKING. |  [optional] |
|**clickTag** | **String** | Tag string to record a click. |  [optional] |
|**creativeId** | **String** | Creative associated with this placement tag. Applicable only when format is PLACEMENT_TAG_TRACKING. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | TagData tag format of this tag. |  [optional] |
|**impressionTag** | **String** | Tag string for serving an ad. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;PLACEMENT_TAG_STANDARD&quot; |
| IFRAME_JAVASCRIPT | &quot;PLACEMENT_TAG_IFRAME_JAVASCRIPT&quot; |
| IFRAME_ILAYER | &quot;PLACEMENT_TAG_IFRAME_ILAYER&quot; |
| INTERNAL_REDIRECT | &quot;PLACEMENT_TAG_INTERNAL_REDIRECT&quot; |
| JAVASCRIPT | &quot;PLACEMENT_TAG_JAVASCRIPT&quot; |
| INTERSTITIAL_IFRAME_JAVASCRIPT | &quot;PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT&quot; |
| INTERSTITIAL_INTERNAL_REDIRECT | &quot;PLACEMENT_TAG_INTERSTITIAL_INTERNAL_REDIRECT&quot; |
| INTERSTITIAL_JAVASCRIPT | &quot;PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT&quot; |
| CLICK_COMMANDS | &quot;PLACEMENT_TAG_CLICK_COMMANDS&quot; |
| INSTREAM_VIDEO_PREFETCH | &quot;PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH&quot; |
| TRACKING | &quot;PLACEMENT_TAG_TRACKING&quot; |
| TRACKING_IFRAME | &quot;PLACEMENT_TAG_TRACKING_IFRAME&quot; |
| TRACKING_JAVASCRIPT | &quot;PLACEMENT_TAG_TRACKING_JAVASCRIPT&quot; |
| INSTREAM_VIDEO_PREFETCH_VAST_3 | &quot;PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_3&quot; |
| IFRAME_JAVASCRIPT_LEGACY | &quot;PLACEMENT_TAG_IFRAME_JAVASCRIPT_LEGACY&quot; |
| JAVASCRIPT_LEGACY | &quot;PLACEMENT_TAG_JAVASCRIPT_LEGACY&quot; |
| INTERSTITIAL_IFRAME_JAVASCRIPT_LEGACY | &quot;PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT_LEGACY&quot; |
| INTERSTITIAL_JAVASCRIPT_LEGACY | &quot;PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT_LEGACY&quot; |
| INSTREAM_VIDEO_PREFETCH_VAST_4 | &quot;PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_4&quot; |
| TRACKING_THIRD_PARTY_MEASUREMENT | &quot;PLACEMENT_TAG_TRACKING_THIRD_PARTY_MEASUREMENT&quot; |



