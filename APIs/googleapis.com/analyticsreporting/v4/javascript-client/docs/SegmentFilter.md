# AnalyticsReportingApi.SegmentFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not** | **Boolean** | If true, match the complement of simple or sequence segment. For example, to match all visits not from \&quot;New York\&quot;, we can define the segment as follows: \&quot;sessionSegment\&quot;: { \&quot;segmentFilters\&quot;: [{ \&quot;simpleSegment\&quot; :{ \&quot;orFiltersForSegment\&quot;: [{ \&quot;segmentFilterClauses\&quot;:[{ \&quot;dimensionFilter\&quot;: { \&quot;dimensionName\&quot;: \&quot;ga:city\&quot;, \&quot;expressions\&quot;: [\&quot;New York\&quot;] } }] }] }, \&quot;not\&quot;: \&quot;True\&quot; }] }, | [optional] 
**sequenceSegment** | [**SequenceSegment**](SequenceSegment.md) |  | [optional] 
**simpleSegment** | [**SimpleSegment**](SimpleSegment.md) |  | [optional] 


