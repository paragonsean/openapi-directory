

# Action


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionDetails** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**cadence** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Datetime of when the Action was created |  [optional] |
|**due** | **Boolean** | Whether this step is due |  [optional] |
|**dueOn** | **OffsetDateTime** | When action is due |  [optional] |
|**id** | **Integer** | ID of Action |  [optional] |
|**multitouchGroupId** | **Integer** | ID of the multitouch group |  [optional] |
|**person** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**status** | **String** | The current state of the person on the cadence. Possible values are:  in_progress: this action has not been completed  pending_activity: this action has been acted upon, but the action has not been completed. (i.e. the email is scheduled to send, but has not been delivered yet)  |  [optional] |
|**step** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**type** | **String** | The type of this action. Valid types are: email, phone, other. New types may be added in the future.  |  [optional] |
|**updatedAt** | **OffsetDateTime** | Datetime of when the Action was last updated |  [optional] |
|**user** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |



