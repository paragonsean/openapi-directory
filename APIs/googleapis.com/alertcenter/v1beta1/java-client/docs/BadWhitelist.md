

# BadWhitelist

Alert for setting the domain or IP that malicious email comes from as whitelisted domain or IP in Gmail advanced settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainId** | [**DomainId**](DomainId.md) |  |  [optional] |
|**maliciousEntity** | [**MaliciousEntity**](MaliciousEntity.md) |  |  [optional] |
|**messages** | [**List&lt;GmailMessageInfo&gt;**](GmailMessageInfo.md) | The list of messages contained by this alert. |  [optional] |
|**sourceIp** | **String** | The source IP address of the malicious email, for example, &#x60;127.0.0.1&#x60;. |  [optional] |



