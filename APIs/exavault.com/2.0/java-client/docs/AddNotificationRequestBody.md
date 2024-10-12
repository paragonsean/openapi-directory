

# AddNotificationRequestBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Type of action be notified about. Notifications will only be fired for the given type of action. Valid choices are **upload**, **download**, **delete** or **all** (upload/download/delete) |  |
|**message** | **String** | Custom message to include in notification emails. |  [optional] |
|**recipients** | **List&lt;String&gt;** | Email addresses to send notification emails to. If not specified, sends to the current user&#39;s email address. |  [optional] |
|**resource** | **String** | Resources for this notification. See details on [how to specify resources](#section/Identifying-Resources) above. |  |
|**sendEmail** | **Boolean** | Set to true if the user should be notified by email when the notification is triggered. |  |
|**type** | [**TypeEnum**](#TypeEnum) | What kind of notification you&#39;re making. Valid choices are:  - **file** to monitor activity for a file resource - **folder** to monitor activity for a folder resource |  |
|**usernames** | **List&lt;String&gt;** | Determines which users&#39; actions should trigger the notification.   Rather than listing  individual users, you can also use 3 special options:  - **notice\\_user\\_all** for activity by any user or share recipient - **notice\\_user\\_all\\_users** for activity only by user accounts - **notice\\_user\\_all\\_recipient** for activity only by share recipients |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| UPLOAD | &quot;upload&quot; |
| DOWNLOAD | &quot;download&quot; |
| DELETE | &quot;delete&quot; |
| ALL | &quot;all&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FILE | &quot;file&quot; |
| FOLDER | &quot;folder&quot; |



