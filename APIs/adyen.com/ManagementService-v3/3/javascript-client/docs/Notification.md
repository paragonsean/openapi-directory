# ManagementApi.Notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The type of event notification sent when you select the notification button. | [optional] 
**details** | **String** | The text shown in the prompt which opens when you select the notification button. For example, the description of the input box for pay-at-table. | [optional] 
**enabled** | **Boolean** | Enables sending event notifications either by pressing the Confirm key on terminals with a keypad or by tapping the event notification button on the terminal screen. | [optional] 
**showButton** | **Boolean** | Shows or hides the event notification button on the screen of terminal models that have a keypad. | [optional] 
**title** | **String** | The name of the notification button on the terminal screen. | [optional] 



## Enum: CategoryEnum


* `SaleWakeUp` (value: `"SaleWakeUp"`)

* `KeyPressed` (value: `"KeyPressed"`)

* `empty` (value: `""`)




