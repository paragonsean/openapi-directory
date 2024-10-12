# AppConfigurationManagementClient.PrivateLinkServiceConnectionState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionsRequired** | **String** | Any action that is required beyond basic workflow (approve/ reject/ disconnect) | [optional] [readonly] 
**description** | **String** | The private link service connection description. | [optional] 
**status** | **String** | The private link service connection status. | [optional] 



## Enum: ActionsRequiredEnum


* `None` (value: `"None"`)

* `Recreate` (value: `"Recreate"`)





## Enum: StatusEnum


* `Pending` (value: `"Pending"`)

* `Approved` (value: `"Approved"`)

* `Rejected` (value: `"Rejected"`)

* `Disconnected` (value: `"Disconnected"`)




