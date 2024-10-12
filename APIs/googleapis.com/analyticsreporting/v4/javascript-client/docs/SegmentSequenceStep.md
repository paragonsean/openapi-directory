# AnalyticsReportingApi.SegmentSequenceStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matchType** | **String** | Specifies if the step immediately precedes or can be any time before the next step. | [optional] 
**orFiltersForSegment** | [**[OrFiltersForSegment]**](OrFiltersForSegment.md) | A sequence is specified with a list of Or grouped filters which are combined with &#x60;AND&#x60; operator. | [optional] 



## Enum: MatchTypeEnum


* `UNSPECIFIED_MATCH_TYPE` (value: `"UNSPECIFIED_MATCH_TYPE"`)

* `PRECEDES` (value: `"PRECEDES"`)

* `IMMEDIATELY_PRECEDES` (value: `"IMMEDIATELY_PRECEDES"`)




