

# GoogleAnalyticsAdminV1alphaAudienceEventTrigger

Specifies an event to log when a user joins the Audience.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventName** | **String** | Required. The event name that will be logged. |  [optional] |
|**logCondition** | [**LogConditionEnum**](#LogConditionEnum) | Required. When to log the event. |  [optional] |



## Enum: LogConditionEnum

| Name | Value |
|---- | -----|
| LOG_CONDITION_UNSPECIFIED | &quot;LOG_CONDITION_UNSPECIFIED&quot; |
| AUDIENCE_JOINED | &quot;AUDIENCE_JOINED&quot; |
| AUDIENCE_MEMBERSHIP_RENEWED | &quot;AUDIENCE_MEMBERSHIP_RENEWED&quot; |



