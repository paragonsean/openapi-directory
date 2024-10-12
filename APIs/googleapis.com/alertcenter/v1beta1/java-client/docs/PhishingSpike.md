

# PhishingSpike

Alert for a spike in user reported phishing. *Warning*: This type has been deprecated. Use [MailPhishing](/admin-sdk/alertcenter/reference/rest/v1beta1/MailPhishing) instead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainId** | [**DomainId**](DomainId.md) |  |  [optional] |
|**isInternal** | **Boolean** | If &#x60;true&#x60;, the email originated from within the organization. |  [optional] |
|**maliciousEntity** | [**MaliciousEntity**](MaliciousEntity.md) |  |  [optional] |
|**messages** | [**List&lt;GmailMessageInfo&gt;**](GmailMessageInfo.md) | The list of messages contained by this alert. |  [optional] |



