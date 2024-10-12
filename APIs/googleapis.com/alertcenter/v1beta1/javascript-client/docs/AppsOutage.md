# GoogleWorkspaceAlertCenterApi.AppsOutage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboardUri** | **String** | Link to the outage event in Google Workspace Status Dashboard | [optional] 
**incidentTrackingId** | **String** | Incident tracking ID. | [optional] 
**mergeInfo** | [**MergeInfo**](MergeInfo.md) |  | [optional] 
**nextUpdateTime** | **String** | Timestamp by which the next update is expected to arrive. | [optional] 
**products** | **[String]** | List of products impacted by the outage. | [optional] 
**resolutionTime** | **String** | Timestamp when the outage is expected to be resolved, or has confirmed resolution. Provided only when known. | [optional] 
**status** | **String** | Current outage status. | [optional] 



## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `NEW` (value: `"NEW"`)

* `ONGOING` (value: `"ONGOING"`)

* `RESOLVED` (value: `"RESOLVED"`)

* `FALSE_POSITIVE` (value: `"FALSE_POSITIVE"`)

* `PARTIALLY_RESOLVED` (value: `"PARTIALLY_RESOLVED"`)

* `MERGED` (value: `"MERGED"`)

* `DOWNGRADED` (value: `"DOWNGRADED"`)




