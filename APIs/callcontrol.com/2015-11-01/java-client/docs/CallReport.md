

# CallReport

Call Report  PhoneNumber,   Caller name(optional),   Call category(optional),   Comment or tags(free text) (optional),   Unwanted call  - yes/no(optional),

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callTime** | **OffsetDateTime** |  |  [optional] |
|**callerType** | [**CallerTypeEnum**](#CallerTypeEnum) |  |  [optional] |
|**comment** | **String** |  |  [optional] |
|**ipAddress** | **String** |  |  [optional] |
|**latitude** | **Double** |  |  [optional] |
|**longitude** | **Double** |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**reportedCallerId** | **String** |  |  [optional] |
|**reportedCallerName** | **String** |  |  [optional] |
|**reporter** | **String** |  |  [optional] |
|**unwantedCall** | **Boolean** |  |  [optional] |



## Enum: CallerTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| TELEMARKETING | &quot;Telemarketing&quot; |
| COLLECTION_AGENCY | &quot;Collection_Agency&quot; |
| POLITICAL | &quot;Political&quot; |
| SURVEYOR | &quot;Surveyor&quot; |
| PRANK_CALL | &quot;Prank_Call&quot; |
| FUND_RAISER | &quot;Fund_Raiser&quot; |
| OTHER_COMMERCIAL | &quot;Other_Commercial&quot; |
| SCAM | &quot;Scam&quot; |
| VOIP | &quot;VOIP&quot; |
| BUSINESS | &quot;Business&quot; |
| REMINDER_NOTIFICATION_CALL | &quot;Reminder_Notification_Call&quot; |
| JUNK_FAX | &quot;Junk_Fax&quot; |
| FAX_MACHINE | &quot;Fax_Machine&quot; |
| SPAM_TEXT | &quot;Spam_Text&quot; |
| ROBO_CALL | &quot;RoboCall&quot; |
| NOT_SPAM | &quot;NotSpam&quot; |
| CALLBACK | &quot;Callback&quot; |



