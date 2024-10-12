

# GoogleChecksReportV1alphaCheckStateMetadata

Additional information about the check state in relation to past reports.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**badges** | [**List&lt;BadgesEnum&gt;**](#List&lt;BadgesEnum&gt;) | Indicators related to the check state. |  [optional] |
|**firstFailingTime** | **String** | The time when the check first started failing. |  [optional] |
|**lastFailingTime** | **String** | The last time the check failed. |  [optional] |



## Enum: List&lt;BadgesEnum&gt;

| Name | Value |
|---- | -----|
| CHECK_STATE_BADGE_UNSPECIFIED | &quot;CHECK_STATE_BADGE_UNSPECIFIED&quot; |
| NEWLY_FAILING | &quot;NEWLY_FAILING&quot; |
| RECENTLY_FAILING | &quot;RECENTLY_FAILING&quot; |
| RESOLVED | &quot;RESOLVED&quot; |



