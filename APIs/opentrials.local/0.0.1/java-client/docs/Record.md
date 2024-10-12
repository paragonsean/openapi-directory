

# Record


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Date when the record was created |  |
|**id** | **String** | ID of the record |  |
|**identifiers** | **Object** | Object that maps the trial&#39;s sources ids with its identifiers. |  [optional] |
|**isPrimary** | **Boolean** | Is this record the primary source of data for its trial |  [optional] |
|**lastVerificationDate** | **OffsetDateTime** | Date when the record&#39;s data was last verified by provider |  [optional] |
|**publicTitle** | **String** | Title of the record |  |
|**recruitmentStatus** | [**RecruitmentStatusEnum**](#RecruitmentStatusEnum) | Trial&#39;s recruitment status (e.g. recruiting, unknown etc.) |  [optional] |
|**source** | [**Source**](Source.md) |  |  |
|**sourceId** | **String** | ID of the record&#39;s source |  [optional] |
|**sourceUrl** | **String** | URL of the record&#39;s source (where it was collected from) |  |
|**status** | [**StatusEnum**](#StatusEnum) | Trial&#39;s status (e.g. ongoing, withdrawn, complete etc.) |  [optional] |
|**trialId** | **String** | ID of the trial referenced in the record |  |
|**trialUrl** | **String** | OpenTrials API URL of the trial referenced in the record |  |
|**updatedAt** | **OffsetDateTime** | Date when the record was updated |  |
|**url** | **String** | OpenTrials API URL of the record |  |



## Enum: RecruitmentStatusEnum

| Name | Value |
|---- | -----|
| RECRUITING | &quot;recruiting&quot; |
| NOT_RECRUITING | &quot;not_recruiting&quot; |
| UNKNOWN | &quot;unknown&quot; |
| OTHER | &quot;other&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ONGOING | &quot;ongoing&quot; |
| WITHDRAWN | &quot;withdrawn&quot; |
| SUSPENDED | &quot;suspended&quot; |
| TERMINATED | &quot;terminated&quot; |
| COMPLETE | &quot;complete&quot; |
| UNKNOWN | &quot;unknown&quot; |
| OTHER | &quot;other&quot; |



