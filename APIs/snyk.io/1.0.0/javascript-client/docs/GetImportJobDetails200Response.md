# SnykApi.GetImportJobDetails200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **String** | the time when an import job was created represented as a [UTC (ISO-8601)](https://tools.ietf.org/html/rfc3339) string | [optional] 
**id** | **String** | A uuid representing the job&#39;s id | [optional] 
**logs** | **[Object]** | all organizations imported by the job | [optional] 
**status** | **String** | a string representing the status of a job.  One of: pending, failed, aborted or complete. | [optional] 


