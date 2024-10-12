

# SettingsResponse

Webhook settings for an app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | When this subscription was created. Formatted as milliseconds from the [Unix epoch](#). |  |
|**targetUrl** | **String** | A publicly available URL for HubSpot to call where event payloads will be delivered. See [link-so-some-doc](#) for details about the format of these event payloads. |  |
|**throttling** | [**ThrottlingSettings**](ThrottlingSettings.md) |  |  |
|**updatedAt** | **OffsetDateTime** | When this subscription was last updated. Formatted as milliseconds from the [Unix epoch](#). |  [optional] |



