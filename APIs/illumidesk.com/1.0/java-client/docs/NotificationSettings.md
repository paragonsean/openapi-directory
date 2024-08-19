

# NotificationSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailAddress** | **String** | Email address to send notifications. |  [optional] |
|**emailsEnabled** | **Boolean** | Turn emails on or off. |  |
|**enabled** | **Boolean** | Turn notifications on or off entirely. |  |
|**entity** | [**EntityEnum**](#EntityEnum) | The entity type that the settings pertain to. |  [optional] |
|**id** | **String** | Notification unique identifier expressed as a UUID |  [optional] |
|**user** | **String** | User the notification settings is for. |  [optional] |



## Enum: EntityEnum

| Name | Value |
|---- | -----|
| GLOBAL | &quot;global&quot; |
| BILLING | &quot;billing&quot; |



