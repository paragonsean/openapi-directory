

# TaskrouterV1WorkspaceTask


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Task resource. |  [optional] |
|**addons** | **String** | An object that contains the [Add-on](https://www.twilio.com/docs/add-ons) data for all installed Add-ons. |  [optional] |
|**age** | **Integer** | The number of seconds since the Task was created. |  [optional] |
|**assignmentStatus** | **TaskEnumStatus** |  |  [optional] |
|**attributes** | **String** | The JSON string with custom attributes of the work. **Note** If this property has been assigned a value, it will only be displayed in FETCH action that returns a single resource. Otherwise, it will be null. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**priority** | **Integer** | The current priority score of the Task as assigned to a Worker by the workflow. Tasks with higher priority values will be assigned before Tasks with lower values. |  [optional] |
|**reason** | **String** | The reason the Task was canceled or completed, if applicable. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Task resource. |  [optional] |
|**taskChannelSid** | **String** | The SID of the TaskChannel. |  [optional] |
|**taskChannelUniqueName** | **String** | The unique name of the TaskChannel. |  [optional] |
|**taskQueueEnteredDate** | **OffsetDateTime** | The date and time in GMT when the Task entered the TaskQueue, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**taskQueueFriendlyName** | **String** | The friendly name of the TaskQueue. |  [optional] |
|**taskQueueSid** | **String** | The SID of the TaskQueue. |  [optional] |
|**timeout** | **Integer** | The amount of time in seconds that the Task can live before being assigned. |  [optional] |
|**url** | **URI** | The absolute URL of the Task resource. |  [optional] |
|**virtualStartTime** | **OffsetDateTime** | The date and time in GMT indicating the ordering for routing of the Task specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**workflowFriendlyName** | **String** | The friendly name of the Workflow that is controlling the Task. |  [optional] |
|**workflowSid** | **String** | The SID of the Workflow that is controlling the Task. |  [optional] |
|**workspaceSid** | **String** | The SID of the Workspace that contains the Task. |  [optional] |



