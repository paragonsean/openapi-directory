

# GooglePlayDeveloperReportingV1alpha1FreshnessInfo

Represents the latest available time that can be requested in a TimelineSpec. Different aggregation periods have different freshness. For example, `DAILY` aggregation may lag behind `HOURLY` in cases where such aggregation is computed only once at the end of the day.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**freshnesses** | [**List&lt;GooglePlayDeveloperReportingV1alpha1FreshnessInfoFreshness&gt;**](GooglePlayDeveloperReportingV1alpha1FreshnessInfoFreshness.md) | Information about data freshness for every supported aggregation period. This field has set semantics, keyed by the &#x60;aggregation_period&#x60; field. |  [optional] |



