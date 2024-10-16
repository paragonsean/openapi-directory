# ExaVault.AddNotificationRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Type of action be notified about. Notifications will only be fired for the given type of action. Valid choices are **upload**, **download**, **delete** or **all** (upload/download/delete) | 
**message** | **String** | Custom message to include in notification emails. | [optional] 
**recipients** | **[String]** | Email addresses to send notification emails to. If not specified, sends to the current user&#39;s email address. | [optional] 
**resource** | **String** | Resources for this notification. See details on [how to specify resources](#section/Identifying-Resources) above. | 
**sendEmail** | **Boolean** | Set to true if the user should be notified by email when the notification is triggered. | 
**type** | **String** | What kind of notification you&#39;re making. Valid choices are:  - **file** to monitor activity for a file resource - **folder** to monitor activity for a folder resource | 
**usernames** | **[String]** | Determines which users&#39; actions should trigger the notification.   Rather than listing  individual users, you can also use 3 special options:  - **notice\\_user\\_all** for activity by any user or share recipient - **notice\\_user\\_all\\_users** for activity only by user accounts - **notice\\_user\\_all\\_recipient** for activity only by share recipients | 



## Enum: ActionEnum


* `upload` (value: `"upload"`)

* `download` (value: `"download"`)

* `delete` (value: `"delete"`)

* `all` (value: `"all"`)





## Enum: TypeEnum


* `file` (value: `"file"`)

* `folder` (value: `"folder"`)




