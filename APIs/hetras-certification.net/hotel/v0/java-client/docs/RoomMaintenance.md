

# RoomMaintenance


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | **String** | Start date of the current maintenance work |  [optional] |
|**reason** | **String** | A description about the reason for the ongoing maintenance work |  [optional] |
|**to** | **String** | End date of the current maintenance work |  [optional] |
|**value** | [**ValueEnum**](#ValueEnum) | Maintenance Status |  [optional] |



## Enum: ValueEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| NONE | &quot;None&quot; |
| OUT_OF_INVENTORY | &quot;OutOfInventory&quot; |
| OUT_OF_ORDER | &quot;OutOfOrder&quot; |
| OUT_OF_SERVICE | &quot;OutOfService&quot; |



