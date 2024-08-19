# GitHubV3RestApi.ChecksUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[ChecksCreateRequestActionsInner]**](ChecksCreateRequestActionsInner.md) | Possible further actions the integrator can perform, which a user may trigger. Each action includes a &#x60;label&#x60;, &#x60;identifier&#x60; and &#x60;description&#x60;. A maximum of three actions are accepted. See the [&#x60;actions&#x60; object](https://docs.github.com/enterprise-server@3.1/rest/reference/checks#actions-object) description. To learn more about check runs and requested actions, see \&quot;[Check runs and requested actions](https://docs.github.com/enterprise-server@3.1/rest/reference/checks#check-runs-and-requested-actions).\&quot; | [optional] 
**completedAt** | **Date** | The time the check completed. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
**conclusion** | **String** | **Required if you provide &#x60;completed_at&#x60; or a &#x60;status&#x60; of &#x60;completed&#x60;**. The final conclusion of the check.  **Note:** Providing &#x60;conclusion&#x60; will automatically set the &#x60;status&#x60; parameter to &#x60;completed&#x60;. You cannot change a check run conclusion to &#x60;stale&#x60;, only GitHub can set this. | [optional] 
**detailsUrl** | **String** | The URL of the integrator&#39;s site that has the full details of the check. | [optional] 
**externalId** | **String** | A reference for the run on the integrator&#39;s system. | [optional] 
**name** | **String** | The name of the check. For example, \&quot;code-coverage\&quot;. | [optional] 
**output** | [**ChecksUpdateRequestOutput**](ChecksUpdateRequestOutput.md) |  | [optional] 
**startedAt** | **Date** | This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
**status** | **String** | The current status. | [optional] 



## Enum: ConclusionEnum


* `action_required` (value: `"action_required"`)

* `cancelled` (value: `"cancelled"`)

* `failure` (value: `"failure"`)

* `neutral` (value: `"neutral"`)

* `success` (value: `"success"`)

* `skipped` (value: `"skipped"`)

* `stale` (value: `"stale"`)

* `timed_out` (value: `"timed_out"`)





## Enum: StatusEnum


* `queued` (value: `"queued"`)

* `in_progress` (value: `"in_progress"`)

* `completed` (value: `"completed"`)




