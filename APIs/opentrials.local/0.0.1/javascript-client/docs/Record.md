# OpenTrialsApi.Record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | Date when the record was created | 
**id** | **String** | ID of the record | 
**identifiers** | **Object** | Object that maps the trial&#39;s sources ids with its identifiers. | [optional] 
**isPrimary** | **Boolean** | Is this record the primary source of data for its trial | [optional] 
**lastVerificationDate** | **Date** | Date when the record&#39;s data was last verified by provider | [optional] 
**publicTitle** | **String** | Title of the record | 
**recruitmentStatus** | **String** | Trial&#39;s recruitment status (e.g. recruiting, unknown etc.) | [optional] 
**source** | [**Source**](Source.md) |  | 
**sourceId** | **String** | ID of the record&#39;s source | [optional] 
**sourceUrl** | **String** | URL of the record&#39;s source (where it was collected from) | 
**status** | **String** | Trial&#39;s status (e.g. ongoing, withdrawn, complete etc.) | [optional] 
**trialId** | **String** | ID of the trial referenced in the record | 
**trialUrl** | **String** | OpenTrials API URL of the trial referenced in the record | 
**updatedAt** | **Date** | Date when the record was updated | 
**url** | **String** | OpenTrials API URL of the record | 



## Enum: RecruitmentStatusEnum


* `recruiting` (value: `"recruiting"`)

* `not_recruiting` (value: `"not_recruiting"`)

* `unknown` (value: `"unknown"`)

* `other` (value: `"other"`)





## Enum: StatusEnum


* `ongoing` (value: `"ongoing"`)

* `withdrawn` (value: `"withdrawn"`)

* `suspended` (value: `"suspended"`)

* `terminated` (value: `"terminated"`)

* `complete` (value: `"complete"`)

* `unknown` (value: `"unknown"`)

* `other` (value: `"other"`)




