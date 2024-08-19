

# AppPkgNotification

'This data type represents an application package management notification for informing the subscribers about onboarding application package resources. The notification is triggered when a new application package is onboarded'

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**AppPkgNotificationLinks**](AppPkgNotificationLinks.md) |  |  |
|**appDId** | **String** | Identifier of this MEC application descriptor. This attribute shall be globally unique. |  |
|**appPkgId** | **String** | Identifier of the onboarded application package. |  |
|**id** | **String** | &#39;&#39; |  |
|**notificationType** | **AppPkgNotificationType** |  |  |
|**operationalState** | [**OperationalStateEnum**](#OperationalStateEnum) |  |  |
|**subscriptionId** | **String** | Identifier of the subscription related to this notification. |  |
|**timeStamp** | [**TimeStamp**](TimeStamp.md) |  |  |



## Enum: OperationalStateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;DISABLED&quot; |
| ENABLED | &quot;ENABLED&quot; |



