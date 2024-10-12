

# AutomationEntity

List Automations

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automation** | [**AutomationEnum**](#AutomationEnum) | Automation type |  [optional] |
|**deleted** | **Boolean** | Indicates if the automation has been deleted. |  [optional] |
|**description** | **String** | Description for the this Automation. |  [optional] |
|**destinationReplaceFrom** | **String** | If set, this string in the destination path will be replaced with the value in &#x60;destination_replace_to&#x60;. |  [optional] |
|**destinationReplaceTo** | **String** | If set, this string will replace the value &#x60;destination_replace_from&#x60; in the destination filename. You can use special patterns here. |  [optional] |
|**destinations** | **List&lt;String&gt;** | Destination Path |  [optional] |
|**disabled** | **Boolean** | If true, this automation will not run. |  [optional] |
|**groupIds** | **List&lt;Integer&gt;** | IDs of Groups for the Automation (i.e. who to Request File from) |  [optional] |
|**id** | **Integer** | Automation ID |  [optional] |
|**interval** | **String** | If trigger is &#x60;daily&#x60;, this specifies how often to run this automation.  One of: &#x60;day&#x60;, &#x60;week&#x60;, &#x60;week_end&#x60;, &#x60;month&#x60;, &#x60;month_end&#x60;, &#x60;quarter&#x60;, &#x60;quarter_end&#x60;, &#x60;year&#x60;, &#x60;year_end&#x60; |  [optional] |
|**lastModifiedAt** | **OffsetDateTime** | Time when automation was last modified. Does not change for name or description updates. |  [optional] |
|**name** | **String** | Name for this automation. |  [optional] |
|**path** | **String** | Path on which this Automation runs.  Supports globs. |  [optional] |
|**recurringDay** | **Integer** | If trigger type is &#x60;daily&#x60;, this specifies a day number to run in one of the supported intervals: &#x60;week&#x60;, &#x60;month&#x60;, &#x60;quarter&#x60;, &#x60;year&#x60;. |  [optional] |
|**schedule** | **Object** | If trigger is &#x60;custom_schedule&#x60;, Custom schedule description for when the automation should be run. |  [optional] |
|**source** | **String** | Source Path |  [optional] |
|**syncIds** | **List&lt;Integer&gt;** | IDs of remote sync folder behaviors to run by this Automation |  [optional] |
|**trigger** | [**TriggerEnum**](#TriggerEnum) | How this automation is triggered to run. One of: &#x60;realtime&#x60;, &#x60;daily&#x60;, &#x60;custom_schedule&#x60;, &#x60;webhook&#x60;, &#x60;email&#x60;, or &#x60;action&#x60;. |  [optional] |
|**triggerActions** | **List&lt;String&gt;** | If trigger is &#x60;action&#x60;, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy |  [optional] |
|**userId** | **Integer** | User ID of the Automation&#39;s creator. |  [optional] |
|**userIds** | **List&lt;Integer&gt;** | IDs of Users for the Automation (i.e. who to Request File from) |  [optional] |
|**value** | **Object** | A Hash of attributes specific to the automation type. |  [optional] |
|**webhookUrl** | **String** | If trigger is &#x60;webhook&#x60;, this is the URL of the webhook to trigger the Automation. |  [optional] |



## Enum: AutomationEnum

| Name | Value |
|---- | -----|
| CREATE_FOLDER | &quot;create_folder&quot; |
| REQUEST_FILE | &quot;request_file&quot; |
| REQUEST_MOVE | &quot;request_move&quot; |
| COPY_NEWEST_FILE | &quot;copy_newest_file&quot; |
| DELETE_FILE | &quot;delete_file&quot; |
| COPY_FILE | &quot;copy_file&quot; |
| MOVE_FILE | &quot;move_file&quot; |
| AS2_SEND | &quot;as2_send&quot; |
| RUN_SYNC | &quot;run_sync&quot; |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| REALTIME | &quot;realtime&quot; |
| DAILY | &quot;daily&quot; |
| CUSTOM_SCHEDULE | &quot;custom_schedule&quot; |
| WEBHOOK | &quot;webhook&quot; |
| EMAIL | &quot;email&quot; |
| ACTION | &quot;action&quot; |



