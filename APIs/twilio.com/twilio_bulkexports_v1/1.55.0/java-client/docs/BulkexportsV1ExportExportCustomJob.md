

# BulkexportsV1ExportExportCustomJob


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **Object** | The details of a job which is an object that contains an array of status grouped by &#x60;status&#x60; state.  Each &#x60;status&#x60; object has a &#x60;status&#x60; string, a count which is the number of days in that &#x60;status&#x60;, and list of days in that &#x60;status&#x60;. The day strings are in the format yyyy-MM-dd. As an example, a currently running job may have a status object for COMPLETED and a &#x60;status&#x60; object for SUBMITTED each with its own count and list of days. |  [optional] |
|**email** | **String** | The optional email to send the completion notification to |  [optional] |
|**endDay** | **String** | The end day for the export specified when creating the job |  [optional] |
|**estimatedCompletionTime** | **String** | this is the time estimated until your job is complete. This is calculated each time you request the job list. The time is calculated based on the current rate of job completion (which may vary) and your job queue position |  [optional] |
|**friendlyName** | **String** | The friendly name specified when creating the job |  [optional] |
|**jobQueuePosition** | **String** | This is the job position from the 1st in line. Your queue position will never increase. As jobs ahead of yours in the queue are processed, the queue position number will decrease |  [optional] |
|**jobSid** | **String** | The unique job_sid returned when the custom export was created |  [optional] |
|**resourceType** | **String** | The type of communication – Messages, Calls, Conferences, and Participants |  [optional] |
|**startDay** | **String** | The start day for the custom export specified when creating the job |  [optional] |
|**webhookMethod** | **String** | This is the method used to call the webhook on completion of the job. If this is supplied, &#x60;WebhookUrl&#x60; must also be supplied. |  [optional] |
|**webhookUrl** | **String** | The optional webhook url called on completion of the job. If this is supplied, &#x60;WebhookMethod&#x60; must also be supplied. |  [optional] |



