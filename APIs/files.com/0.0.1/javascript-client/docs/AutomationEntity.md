# FilesComApi.AutomationEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automation** | **String** | Automation type | [optional] 
**deleted** | **Boolean** | Indicates if the automation has been deleted. | [optional] 
**description** | **String** | Description for the this Automation. | [optional] 
**destinationReplaceFrom** | **String** | If set, this string in the destination path will be replaced with the value in &#x60;destination_replace_to&#x60;. | [optional] 
**destinationReplaceTo** | **String** | If set, this string will replace the value &#x60;destination_replace_from&#x60; in the destination filename. You can use special patterns here. | [optional] 
**destinations** | **[String]** | Destination Path | [optional] 
**disabled** | **Boolean** | If true, this automation will not run. | [optional] 
**groupIds** | **[Number]** | IDs of Groups for the Automation (i.e. who to Request File from) | [optional] 
**id** | **Number** | Automation ID | [optional] 
**interval** | **String** | If trigger is &#x60;daily&#x60;, this specifies how often to run this automation.  One of: &#x60;day&#x60;, &#x60;week&#x60;, &#x60;week_end&#x60;, &#x60;month&#x60;, &#x60;month_end&#x60;, &#x60;quarter&#x60;, &#x60;quarter_end&#x60;, &#x60;year&#x60;, &#x60;year_end&#x60; | [optional] 
**lastModifiedAt** | **Date** | Time when automation was last modified. Does not change for name or description updates. | [optional] 
**name** | **String** | Name for this automation. | [optional] 
**path** | **String** | Path on which this Automation runs.  Supports globs. | [optional] 
**recurringDay** | **Number** | If trigger type is &#x60;daily&#x60;, this specifies a day number to run in one of the supported intervals: &#x60;week&#x60;, &#x60;month&#x60;, &#x60;quarter&#x60;, &#x60;year&#x60;. | [optional] 
**schedule** | **Object** | If trigger is &#x60;custom_schedule&#x60;, Custom schedule description for when the automation should be run. | [optional] 
**source** | **String** | Source Path | [optional] 
**syncIds** | **[Number]** | IDs of remote sync folder behaviors to run by this Automation | [optional] 
**trigger** | **String** | How this automation is triggered to run. One of: &#x60;realtime&#x60;, &#x60;daily&#x60;, &#x60;custom_schedule&#x60;, &#x60;webhook&#x60;, &#x60;email&#x60;, or &#x60;action&#x60;. | [optional] 
**triggerActions** | **[String]** | If trigger is &#x60;action&#x60;, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy | [optional] 
**userId** | **Number** | User ID of the Automation&#39;s creator. | [optional] 
**userIds** | **[Number]** | IDs of Users for the Automation (i.e. who to Request File from) | [optional] 
**value** | **Object** | A Hash of attributes specific to the automation type. | [optional] 
**webhookUrl** | **String** | If trigger is &#x60;webhook&#x60;, this is the URL of the webhook to trigger the Automation. | [optional] 



## Enum: AutomationEnum


* `create_folder` (value: `"create_folder"`)

* `request_file` (value: `"request_file"`)

* `request_move` (value: `"request_move"`)

* `copy_newest_file` (value: `"copy_newest_file"`)

* `delete_file` (value: `"delete_file"`)

* `copy_file` (value: `"copy_file"`)

* `move_file` (value: `"move_file"`)

* `as2_send` (value: `"as2_send"`)

* `run_sync` (value: `"run_sync"`)





## Enum: TriggerEnum


* `realtime` (value: `"realtime"`)

* `daily` (value: `"daily"`)

* `custom_schedule` (value: `"custom_schedule"`)

* `webhook` (value: `"webhook"`)

* `email` (value: `"email"`)

* `action` (value: `"action"`)




