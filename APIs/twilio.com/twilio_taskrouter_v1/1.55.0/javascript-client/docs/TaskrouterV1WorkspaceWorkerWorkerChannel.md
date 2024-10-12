# TwilioTaskrouter.TaskrouterV1WorkspaceWorkerWorkerChannel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Worker resource. | [optional] 
**assignedTasks** | **Number** | The total number of Tasks assigned to Worker for the TaskChannel type. | [optional] 
**available** | **Boolean** | Whether the Worker should receive Tasks of the TaskChannel type. | [optional] 
**availableCapacityPercentage** | **Number** | The current percentage of capacity the TaskChannel has available. Can be a number between &#x60;0&#x60; and &#x60;100&#x60;. A value of &#x60;0&#x60; indicates that TaskChannel has no capacity available and a value of &#x60;100&#x60; means the  Worker is available to receive any Tasks of this TaskChannel type. | [optional] 
**configuredCapacity** | **Number** | The current configured capacity for the WorkerChannel. TaskRouter will not create any reservations after the assigned Tasks for the Worker reaches the value. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**sid** | **String** | The unique string that we created to identify the WorkerChannel resource. | [optional] 
**taskChannelSid** | **String** | The SID of the TaskChannel. | [optional] 
**taskChannelUniqueName** | **String** | The unique name of the TaskChannel, such as &#x60;voice&#x60; or &#x60;sms&#x60;. | [optional] 
**url** | **String** | The absolute URL of the WorkerChannel resource. | [optional] 
**workerSid** | **String** | The SID of the Worker that contains the WorkerChannel. | [optional] 
**workspaceSid** | **String** | The SID of the Workspace that contains the WorkerChannel. | [optional] 


