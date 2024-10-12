

# TransferRun

Represents a data transfer run.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceId** | **String** | Output only. Data source id. |  [optional] [readonly] |
|**destinationDatasetId** | **String** | Output only. The BigQuery target dataset id. |  [optional] [readonly] |
|**emailPreferences** | [**EmailPreferences**](EmailPreferences.md) |  |  [optional] |
|**endTime** | **String** | Output only. Time when transfer run ended. Parameter ignored by server for input requests. |  [optional] [readonly] |
|**errorStatus** | [**Status**](Status.md) |  |  [optional] |
|**name** | **String** | The resource name of the transfer run. Transfer run names have the form &#x60;projects/{project_id}/locations/{location}/transferConfigs/{config_id}/runs/{run_id}&#x60;. The name is ignored when creating a transfer run. |  [optional] |
|**notificationPubsubTopic** | **String** | Output only. Pub/Sub topic where a notification will be sent after this transfer run finishes. The format for specifying a pubsub topic is: &#x60;projects/{project_id}/topics/{topic_id}&#x60; |  [optional] [readonly] |
|**params** | **Map&lt;String, Object&gt;** | Output only. Parameters specific to each data source. For more information see the bq tab in the &#39;Setting up a data transfer&#39; section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq |  [optional] [readonly] |
|**runTime** | **String** | For batch transfer runs, specifies the date and time of the data should be ingested. |  [optional] |
|**schedule** | **String** | Output only. Describes the schedule of this transfer run if it was created as part of a regular schedule. For batch transfer runs that are scheduled manually, this is empty. NOTE: the system might choose to delay the schedule depending on the current load, so &#x60;schedule_time&#x60; doesn&#39;t always match this. |  [optional] [readonly] |
|**scheduleTime** | **String** | Minimum time after which a transfer run can be started. |  [optional] |
|**startTime** | **String** | Output only. Time when transfer run was started. Parameter ignored by server for input requests. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Data transfer run state. Ignored for input requests. |  [optional] |
|**updateTime** | **String** | Output only. Last time the data transfer run state was updated. |  [optional] [readonly] |
|**userId** | **String** | Deprecated. Unique ID of the user on whose behalf transfer is done. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| TRANSFER_STATE_UNSPECIFIED | &quot;TRANSFER_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



