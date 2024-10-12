

# AutoHealTriggers

AutoHealTriggers - describes the triggers for auto-heal.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateBytesInKB** | **Integer** | PrivateBytesInKB - Defines a rule based on private bytes |  [optional] |
|**requests** | [**RequestsBasedTrigger**](RequestsBasedTrigger.md) |  |  [optional] |
|**slowRequests** | [**SlowRequestsBasedTrigger**](SlowRequestsBasedTrigger.md) |  |  [optional] |
|**statusCodes** | [**List&lt;StatusCodesBasedTrigger&gt;**](StatusCodesBasedTrigger.md) | StatusCodes - Defines a rule based on status codes |  [optional] |



