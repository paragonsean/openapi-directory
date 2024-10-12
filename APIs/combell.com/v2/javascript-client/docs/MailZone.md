# PublicApi.MailZone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**[Alias]**](Alias.md) | List of aliases on the mail zone&lt;br /&gt;  An alias is an e-mail address (alias) that automatically forwards received e-mails to another e-mail address (destination). | [optional] 
**antiSpam** | [**AntiSpam**](AntiSpam.md) |  | [optional] 
**availableAccounts** | [**[MailZoneAccount]**](MailZoneAccount.md) | List of mail zone accounts with their mailbox size. | [optional] 
**catchAll** | [**CatchAll**](CatchAll.md) |  | [optional] 
**enabled** | **Boolean** | Indicates whether the mail zone is enabled. | [optional] 
**name** | **String** |  | [optional] 
**smtpDomains** | [**[SmtpDomain]**](SmtpDomain.md) | List of extra smtp domains on the mail zone&lt;br /&gt;  SMTP domain names allow you to link multiple domain names to a single e-mail address.&lt;br /&gt;  E-mails sent to an SMTP domain will be caught by the respective e-mail address on the main domain name. | [optional] 


