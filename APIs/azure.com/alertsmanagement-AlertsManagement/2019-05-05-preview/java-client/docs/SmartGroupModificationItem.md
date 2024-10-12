

# SmartGroupModificationItem

smartGroup modification item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | **String** | Modification comments |  [optional] |
|**description** | **String** | Description of the modification |  [optional] |
|**modificationEvent** | [**ModificationEventEnum**](#ModificationEventEnum) | Reason for the modification |  [optional] |
|**modifiedAt** | **String** | Modified date and time |  [optional] |
|**modifiedBy** | **String** | Modified user details (Principal client name) |  [optional] |
|**newValue** | **String** | New value |  [optional] |
|**oldValue** | **String** | Old value |  [optional] |



## Enum: ModificationEventEnum

| Name | Value |
|---- | -----|
| SMART_GROUP_CREATED | &quot;SmartGroupCreated&quot; |
| STATE_CHANGE | &quot;StateChange&quot; |
| ALERT_ADDED | &quot;AlertAdded&quot; |
| ALERT_REMOVED | &quot;AlertRemoved&quot; |



