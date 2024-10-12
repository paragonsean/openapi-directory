

# Breadcrumb

A breadcrumb represent a step preceding a log message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | An action representing the breadcrumb. You can set a custom action or use one of the built-in: click, submit, navigation, request, error. |  [optional] |
|**dateTime** | **OffsetDateTime** | The date and time in UTC of the breadcrumb. If no date and time is provided, we will use the current date and time in UTC. |  [optional] |
|**message** | **String** | A message representing the breadcrumb. This should elaborate on the action. |  [optional] |
|**severity** | **String** | An enum value representing the severity of this breadcrumb. The following values are allowed: Verbose, Debug, Information, Warning, Error, Fatal. |  [optional] |



