

# SegmentSettings

Segment settings for `\"ts\"`, `\"fmp4\"` and `\"vtt\"`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**individualSegments** | **Boolean** | Required. Create an individual segment file. The default is &#x60;false&#x60;. |  [optional] |
|**segmentDuration** | **String** | Duration of the segments in seconds. The default is &#x60;\&quot;6.0s\&quot;&#x60;. Note that &#x60;segmentDuration&#x60; must be greater than or equal to [&#x60;gopDuration&#x60;](#videostream), and &#x60;segmentDuration&#x60; must be divisible by [&#x60;gopDuration&#x60;](#videostream). |  [optional] |



