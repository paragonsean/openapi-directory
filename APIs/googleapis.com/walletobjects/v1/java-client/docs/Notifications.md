

# Notifications

Indicates if the object needs to have notification enabled. We support only one of ExpiryNotification/UpcomingNotification. `expiryNotification` takes precedence over `upcomingNotification`. In other words if `expiryNotification` is set, we ignore the `upcomingNotification` field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiryNotification** | [**ExpiryNotification**](ExpiryNotification.md) |  |  [optional] |
|**upcomingNotification** | [**UpcomingNotification**](UpcomingNotification.md) |  |  [optional] |



