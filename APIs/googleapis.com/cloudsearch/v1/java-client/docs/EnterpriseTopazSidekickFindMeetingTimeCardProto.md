

# EnterpriseTopazSidekickFindMeetingTimeCardProto

Response to find meeting time among a set of people.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonAvailableTimeSlots** | [**List&lt;EnterpriseTopazSidekickTimeSlot&gt;**](EnterpriseTopazSidekickTimeSlot.md) | Slots when all attendees have availability. |  [optional] |
|**invitees** | [**List&lt;EnterpriseTopazSidekickPerson&gt;**](EnterpriseTopazSidekickPerson.md) | Invitees to the event. |  [optional] |
|**requester** | [**EnterpriseTopazSidekickPerson**](EnterpriseTopazSidekickPerson.md) |  |  [optional] |
|**scheduledMeeting** | [**EnterpriseTopazSidekickScheduledMeeting**](EnterpriseTopazSidekickScheduledMeeting.md) |  |  [optional] |
|**skippedInvitees** | [**List&lt;EnterpriseTopazSidekickPerson&gt;**](EnterpriseTopazSidekickPerson.md) | Invitees that have been skipped in the computation, most likely because they are groups. |  [optional] |
|**timeBoundaries** | [**EnterpriseTopazSidekickTimeSlot**](EnterpriseTopazSidekickTimeSlot.md) |  |  [optional] |
|**timezoneId** | **String** | Timezone ID. |  [optional] |



