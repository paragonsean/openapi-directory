

# TaskrouterV1WorkspaceTaskQueue


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the TaskQueue resource. |  [optional] |
|**assignmentActivityName** | **String** | The name of the Activity to assign Workers when a task is assigned for them. |  [optional] |
|**assignmentActivitySid** | **String** | The SID of the Activity to assign Workers when a task is assigned for them. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**maxReservedWorkers** | **Integer** | The maximum number of Workers to reserve for the assignment of a task in the queue. Can be an integer between 1 and 50, inclusive and defaults to 1. |  [optional] |
|**reservationActivityName** | **String** | The name of the Activity to assign Workers once a task is reserved for them. |  [optional] |
|**reservationActivitySid** | **String** | The SID of the Activity to assign Workers once a task is reserved for them. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the TaskQueue resource. |  [optional] |
|**targetWorkers** | **String** | A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example &#x60;&#39;\&quot;language\&quot; &#x3D;&#x3D; \&quot;spanish\&quot;&#39;&#x60; If no TargetWorkers parameter is provided, Tasks will wait in the TaskQueue until they are either deleted or moved to another TaskQueue. Additional examples on how to describing Worker selection criteria below. Defaults to 1&#x3D;&#x3D;1. |  [optional] |
|**taskOrder** | **TaskQueueEnumTaskOrder** |  |  [optional] |
|**url** | **URI** | The absolute URL of the TaskQueue resource. |  [optional] |
|**workspaceSid** | **String** | The SID of the Workspace that contains the TaskQueue. |  [optional] |



