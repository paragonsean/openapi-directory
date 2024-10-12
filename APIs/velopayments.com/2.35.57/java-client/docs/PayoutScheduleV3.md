

# PayoutScheduleV3

Details relating to a payout that was executed via a schedule or is still waiting to be executed

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**notificationsEnabled** | **Boolean** |  |  |
|**scheduleStatus** | **String** | The current status of the payout schedule. One of the following values: SCHEDULED, EXECUTED, FAILED |  |
|**scheduledAt** | **OffsetDateTime** |  |  |
|**scheduledByPrincipalId** | **String** | ID of the user or application that scheduled the payout |  |
|**scheduledFor** | **OffsetDateTime** |  |  |



