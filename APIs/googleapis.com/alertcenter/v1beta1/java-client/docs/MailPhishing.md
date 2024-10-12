

# MailPhishing

Proto for all phishing alerts with common payload. Supported types are any of the following: * User reported phishing * User reported spam spike * Suspicious message reported * Phishing reclassification * Malware reclassification * Gmail potential employee spoofing

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainId** | [**DomainId**](DomainId.md) |  |  [optional] |
|**isInternal** | **Boolean** | If &#x60;true&#x60;, the email originated from within the organization. |  [optional] |
|**maliciousEntity** | [**MaliciousEntity**](MaliciousEntity.md) |  |  [optional] |
|**messages** | [**List&lt;GmailMessageInfo&gt;**](GmailMessageInfo.md) | The list of messages contained by this alert. |  [optional] |
|**systemActionType** | [**SystemActionTypeEnum**](#SystemActionTypeEnum) | System actions on the messages. |  [optional] |



## Enum: SystemActionTypeEnum

| Name | Value |
|---- | -----|
| SYSTEM_ACTION_TYPE_UNSPECIFIED | &quot;SYSTEM_ACTION_TYPE_UNSPECIFIED&quot; |
| NO_OPERATION | &quot;NO_OPERATION&quot; |
| REMOVED_FROM_INBOX | &quot;REMOVED_FROM_INBOX&quot; |



