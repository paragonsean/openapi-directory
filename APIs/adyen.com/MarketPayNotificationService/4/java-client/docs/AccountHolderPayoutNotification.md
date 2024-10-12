

# AccountHolderPayoutNotification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | [**AccountHolderPayoutNotificationContent**](AccountHolderPayoutNotificationContent.md) | Details of the payout to the Account Holder. |  [optional] |
|**eventDate** | **OffsetDateTime** | The date and time when an event has been completed. |  |
|**eventType** | **String** | The event type of the notification. |  |
|**executingUserKey** | **String** | The user or process that has triggered the notification. |  |
|**live** | **Boolean** | Indicates whether the notification originated from the live environment or the test environment. If true, the notification originated from the live environment. If false, the notification originated from the test environment. |  |
|**pspReference** | **String** | The PSP reference of the request from which the notification originates. |  |



