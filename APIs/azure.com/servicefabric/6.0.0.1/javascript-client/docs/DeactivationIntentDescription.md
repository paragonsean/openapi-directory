# ServiceFabricClientApis.DeactivationIntentDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deactivationIntent** | **String** | Describes the intent or reason for deactivating the node. The possible values are following.   - Pause - Indicates that the node should be paused. The value is 1.   - Restart - Indicates that the intent is for the node to be restarted after a short period of time. The value is 2.   - RemoveData - Indicates the intent is for the node to remove data. The value is 3.  | [optional] 



## Enum: DeactivationIntentEnum


* `Pause` (value: `"Pause"`)

* `Restart` (value: `"Restart"`)

* `RemoveData` (value: `"RemoveData"`)




