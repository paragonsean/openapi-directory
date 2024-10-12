

# AppsOutage

An outage incident reported for a Google Workspace service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dashboardUri** | **String** | Link to the outage event in Google Workspace Status Dashboard |  [optional] |
|**incidentTrackingId** | **String** | Incident tracking ID. |  [optional] |
|**mergeInfo** | [**MergeInfo**](MergeInfo.md) |  |  [optional] |
|**nextUpdateTime** | **String** | Timestamp by which the next update is expected to arrive. |  [optional] |
|**products** | **List&lt;String&gt;** | List of products impacted by the outage. |  [optional] |
|**resolutionTime** | **String** | Timestamp when the outage is expected to be resolved, or has confirmed resolution. Provided only when known. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current outage status. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| NEW | &quot;NEW&quot; |
| ONGOING | &quot;ONGOING&quot; |
| RESOLVED | &quot;RESOLVED&quot; |
| FALSE_POSITIVE | &quot;FALSE_POSITIVE&quot; |
| PARTIALLY_RESOLVED | &quot;PARTIALLY_RESOLVED&quot; |
| MERGED | &quot;MERGED&quot; |
| DOWNGRADED | &quot;DOWNGRADED&quot; |



