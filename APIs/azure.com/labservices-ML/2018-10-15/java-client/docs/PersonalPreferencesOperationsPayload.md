

# PersonalPreferencesOperationsPayload

Represents payload for any Environment operations like get, start, stop, connect

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addRemove** | [**AddRemoveEnum**](#AddRemoveEnum) | Enum indicating if user is adding or removing a favorite lab |  [optional] |
|**labAccountResourceId** | **String** | Resource Id of the lab account |  [optional] |
|**labResourceId** | **String** | Resource Id of the lab to add/remove from the favorites list |  [optional] |



## Enum: AddRemoveEnum

| Name | Value |
|---- | -----|
| ADD | &quot;Add&quot; |
| REMOVE | &quot;Remove&quot; |



