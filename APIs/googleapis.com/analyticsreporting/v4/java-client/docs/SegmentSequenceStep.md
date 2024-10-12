

# SegmentSequenceStep

A segment sequence definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchType** | [**MatchTypeEnum**](#MatchTypeEnum) | Specifies if the step immediately precedes or can be any time before the next step. |  [optional] |
|**orFiltersForSegment** | [**List&lt;OrFiltersForSegment&gt;**](OrFiltersForSegment.md) | A sequence is specified with a list of Or grouped filters which are combined with &#x60;AND&#x60; operator. |  [optional] |



## Enum: MatchTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED_MATCH_TYPE | &quot;UNSPECIFIED_MATCH_TYPE&quot; |
| PRECEDES | &quot;PRECEDES&quot; |
| IMMEDIATELY_PRECEDES | &quot;IMMEDIATELY_PRECEDES&quot; |



