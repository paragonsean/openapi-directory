

# JobEvent

An event issued when a job seeker interacts with the application that implements Cloud Talent Solution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobs** | **List&lt;String&gt;** | Required. The job name(s) associated with this event. For example, if this is an impression event, this field contains the identifiers of all jobs shown to the job seeker. If this was a view event, this field contains the identifier of the viewed job. The format is \&quot;projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}\&quot;, for example, \&quot;projects/foo/tenants/bar/jobs/baz\&quot;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of the event (see JobEventType). |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| JOB_EVENT_TYPE_UNSPECIFIED | &quot;JOB_EVENT_TYPE_UNSPECIFIED&quot; |
| IMPRESSION | &quot;IMPRESSION&quot; |
| VIEW | &quot;VIEW&quot; |
| VIEW_REDIRECT | &quot;VIEW_REDIRECT&quot; |
| APPLICATION_START | &quot;APPLICATION_START&quot; |
| APPLICATION_FINISH | &quot;APPLICATION_FINISH&quot; |
| APPLICATION_QUICK_SUBMISSION | &quot;APPLICATION_QUICK_SUBMISSION&quot; |
| APPLICATION_REDIRECT | &quot;APPLICATION_REDIRECT&quot; |
| APPLICATION_START_FROM_SEARCH | &quot;APPLICATION_START_FROM_SEARCH&quot; |
| APPLICATION_REDIRECT_FROM_SEARCH | &quot;APPLICATION_REDIRECT_FROM_SEARCH&quot; |
| APPLICATION_COMPANY_SUBMIT | &quot;APPLICATION_COMPANY_SUBMIT&quot; |
| BOOKMARK | &quot;BOOKMARK&quot; |
| NOTIFICATION | &quot;NOTIFICATION&quot; |
| HIRED | &quot;HIRED&quot; |
| SENT_CV | &quot;SENT_CV&quot; |
| INTERVIEW_GRANTED | &quot;INTERVIEW_GRANTED&quot; |



