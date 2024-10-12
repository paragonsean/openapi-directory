# CloudTalentSolutionApi.JobEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | **[String]** | Required. The job name(s) associated with this event. For example, if this is an impression event, this field contains the identifiers of all jobs shown to the job seeker. If this was a view event, this field contains the identifier of the viewed job. The format is \&quot;projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}\&quot;, for example, \&quot;projects/foo/tenants/bar/jobs/baz\&quot;. | [optional] 
**type** | **String** | Required. The type of the event (see JobEventType). | [optional] 



## Enum: TypeEnum


* `JOB_EVENT_TYPE_UNSPECIFIED` (value: `"JOB_EVENT_TYPE_UNSPECIFIED"`)

* `IMPRESSION` (value: `"IMPRESSION"`)

* `VIEW` (value: `"VIEW"`)

* `VIEW_REDIRECT` (value: `"VIEW_REDIRECT"`)

* `APPLICATION_START` (value: `"APPLICATION_START"`)

* `APPLICATION_FINISH` (value: `"APPLICATION_FINISH"`)

* `APPLICATION_QUICK_SUBMISSION` (value: `"APPLICATION_QUICK_SUBMISSION"`)

* `APPLICATION_REDIRECT` (value: `"APPLICATION_REDIRECT"`)

* `APPLICATION_START_FROM_SEARCH` (value: `"APPLICATION_START_FROM_SEARCH"`)

* `APPLICATION_REDIRECT_FROM_SEARCH` (value: `"APPLICATION_REDIRECT_FROM_SEARCH"`)

* `APPLICATION_COMPANY_SUBMIT` (value: `"APPLICATION_COMPANY_SUBMIT"`)

* `BOOKMARK` (value: `"BOOKMARK"`)

* `NOTIFICATION` (value: `"NOTIFICATION"`)

* `HIRED` (value: `"HIRED"`)

* `SENT_CV` (value: `"SENT_CV"`)

* `INTERVIEW_GRANTED` (value: `"INTERVIEW_GRANTED"`)




