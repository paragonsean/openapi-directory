

# IdentityNotificationAttributes

Represents the notification attributes of an identity, including whether an identity has Amazon Simple Notification Service (Amazon SNS) topics set for bounce, complaint, and/or delivery notifications, and whether feedback forwarding is enabled for bounce and complaint notifications.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bounceTopic** | [**String**](String.md) |  |  |
|**complaintTopic** | [**String**](String.md) |  |  |
|**deliveryTopic** | [**String**](String.md) |  |  |
|**forwardingEnabled** | [**Boolean**](Boolean.md) |  |  |
|**headersInBounceNotificationsEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**headersInComplaintNotificationsEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**headersInDeliveryNotificationsEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |



