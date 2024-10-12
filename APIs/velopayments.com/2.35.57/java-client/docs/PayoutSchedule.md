

# PayoutSchedule

Details relating to a payout that was executed via a schedule or is still waiting to be executed

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**notificationsEnabled** | **Boolean** |  |  |
|**scheduleStatus** | **String** | Current status of the payout schedule. One of the following values: SCHEDULED, EXECUTED, FAILED |  |
|**scheduledAt** | **OffsetDateTime** |  |  |
|**scheduledBy** | **String** | Optional display name as a hint for who scheduled the payout. Not populated if payout was scheduled by an application. |  [optional] |
|**scheduledByPrincipalId** | **String** | ID of the user or application that scheduled the payout |  |
|**scheduledFor** | **OffsetDateTime** |  |  |



