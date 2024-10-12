

# UpdateNotificationByIdRequestBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Type of action be notified about. Notifications will only be sent for the given type of action. Valid choices are **upload**, **download**, **delete** or **all** (upload/download/delete) |  [optional] |
|**message** | **String** | Custom message to insert into the notification emails, along with the matching activity. |  [optional] |
|**recipients** | **List&lt;String&gt;** | Email addresses to send notification emails to. If empty, sends to the current user&#39;s email address. |  [optional] |
|**sendEmail** | **Boolean** | Whether an email should be sent to the recipients when matching activity happens. |  [optional] |
|**usernames** | **List&lt;String&gt;** | Determines which users&#39; actions should trigger the notification.   Rather than listing  individual users, you can also use 3 special options:  - **notice\\_user\\_all** for activity by any user or share recipient - **notice\\_user\\_all\\_users** for activity only by user accounts - **notice\\_user\\_all\\_recipients** for activity only by share recipients |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| UPLOAD | &quot;upload&quot; |
| DOWNLOAD | &quot;download&quot; |
| DELETE | &quot;delete&quot; |
| ALL | &quot;all&quot; |



