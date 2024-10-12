

# GoogleCloudRecommenderV1ReliabilityProjection

Contains information on the impact of a reliability recommendation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **Map&lt;String, Object&gt;** | Per-recommender projection. |  [optional] |
|**risks** | [**List&lt;RisksEnum&gt;**](#List&lt;RisksEnum&gt;) | Reliability risks mitigated by this recommendation. |  [optional] |



## Enum: List&lt;RisksEnum&gt;

| Name | Value |
|---- | -----|
| RISK_TYPE_UNSPECIFIED | &quot;RISK_TYPE_UNSPECIFIED&quot; |
| SERVICE_DISRUPTION | &quot;SERVICE_DISRUPTION&quot; |
| DATA_LOSS | &quot;DATA_LOSS&quot; |
| ACCESS_DENY | &quot;ACCESS_DENY&quot; |



