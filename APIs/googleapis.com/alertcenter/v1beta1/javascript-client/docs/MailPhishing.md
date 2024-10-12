# GoogleWorkspaceAlertCenterApi.MailPhishing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainId** | [**DomainId**](DomainId.md) |  | [optional] 
**isInternal** | **Boolean** | If &#x60;true&#x60;, the email originated from within the organization. | [optional] 
**maliciousEntity** | [**MaliciousEntity**](MaliciousEntity.md) |  | [optional] 
**messages** | [**[GmailMessageInfo]**](GmailMessageInfo.md) | The list of messages contained by this alert. | [optional] 
**systemActionType** | **String** | System actions on the messages. | [optional] 



## Enum: SystemActionTypeEnum


* `SYSTEM_ACTION_TYPE_UNSPECIFIED` (value: `"SYSTEM_ACTION_TYPE_UNSPECIFIED"`)

* `NO_OPERATION` (value: `"NO_OPERATION"`)

* `REMOVED_FROM_INBOX` (value: `"REMOVED_FROM_INBOX"`)




