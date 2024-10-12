# BigQueryApi.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**JobConfiguration**](JobConfiguration.md) |  | [optional] 
**etag** | **String** | Output only. A hash of this resource. | [optional] [readonly] 
**id** | **String** | Output only. Opaque ID field of the job. | [optional] [readonly] 
**jobCreationReason** | [**JobCreationReason**](JobCreationReason.md) |  | [optional] 
**jobReference** | [**JobReference**](JobReference.md) |  | [optional] 
**kind** | **String** | Output only. The type of the resource. | [optional] [readonly] [default to &#39;bigquery#job&#39;]
**principalSubject** | **String** | Output only. [Full-projection-only] String representation of identity of requesting party. Populated for both first- and third-party identities. Only present for APIs that support third-party identities. | [optional] [readonly] 
**selfLink** | **String** | Output only. A URL that can be used to access the resource again. | [optional] [readonly] 
**statistics** | [**JobStatistics**](JobStatistics.md) |  | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**userEmail** | **String** | Output only. Email address of the user who ran the job. | [optional] [readonly] 


