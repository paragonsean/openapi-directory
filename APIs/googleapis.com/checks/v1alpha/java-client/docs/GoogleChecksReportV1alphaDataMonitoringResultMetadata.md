

# GoogleChecksReportV1alphaDataMonitoringResultMetadata

Information about a data monitoring result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**badges** | [**List&lt;BadgesEnum&gt;**](#List&lt;BadgesEnum&gt;) | Badges that apply to this result. |  [optional] |
|**firstDetectedTime** | **String** | The timestamp when this result was first detected within the last 8 weeks. If not set, it wasn&#39;t detected within the last 8 weeks. |  [optional] |
|**lastDetectedAppVersion** | **String** | Your app&#39;s version name when this result was last detected within the last 8 weeks. If not set, it wasn&#39;t detected within the last 8 weeks. |  [optional] |
|**lastDetectedTime** | **String** | The timestamp when this result was last detected within the last 8 weeks. If not set, it wasn&#39;t detected within the last 8 weeks. |  [optional] |



## Enum: List&lt;BadgesEnum&gt;

| Name | Value |
|---- | -----|
| DATA_MONITORING_RESULT_BADGE_UNSPECIFIED | &quot;DATA_MONITORING_RESULT_BADGE_UNSPECIFIED&quot; |
| NEW | &quot;NEW&quot; |



