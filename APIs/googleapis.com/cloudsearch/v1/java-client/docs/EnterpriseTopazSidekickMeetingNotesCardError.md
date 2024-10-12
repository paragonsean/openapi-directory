

# EnterpriseTopazSidekickMeetingNotesCardError

Errors in the creation of meeting notes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the reason why create-meeting-notes failed. |  [optional] |
|**event** | [**EnterpriseTopazSidekickAgendaEntry**](EnterpriseTopazSidekickAgendaEntry.md) |  |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason why create-meeting-notes failed. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| NOT_OWNER | &quot;NOT_OWNER&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



