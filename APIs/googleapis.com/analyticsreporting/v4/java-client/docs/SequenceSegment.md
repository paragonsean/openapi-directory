

# SequenceSegment

Sequence conditions consist of one or more steps, where each step is defined by one or more dimension/metric conditions. Multiple steps can be combined with special sequence operators.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstStepShouldMatchFirstHit** | **Boolean** | If set, first step condition must match the first hit of the visitor (in the date range). |  [optional] |
|**segmentSequenceSteps** | [**List&lt;SegmentSequenceStep&gt;**](SegmentSequenceStep.md) | The list of steps in the sequence. |  [optional] |



