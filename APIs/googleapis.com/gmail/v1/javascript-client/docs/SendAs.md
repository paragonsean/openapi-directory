# GmailApi.SendAs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | A name that appears in the \&quot;From:\&quot; header for mail sent using this alias. For custom \&quot;from\&quot; addresses, when this is empty, Gmail will populate the \&quot;From:\&quot; header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail. | [optional] 
**isDefault** | **Boolean** | Whether this address is selected as the default \&quot;From:\&quot; address in situations such as composing a new message or sending a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients may write to this field is &#x60;true&#x60;. Changing this from &#x60;false&#x60; to &#x60;true&#x60; for an address will result in this field becoming &#x60;false&#x60; for the other previous default address. | [optional] 
**isPrimary** | **Boolean** | Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases. This field is read-only. | [optional] 
**replyToAddress** | **String** | An optional email address that is included in a \&quot;Reply-To:\&quot; header for mail sent using this alias. If this is empty, Gmail will not generate a \&quot;Reply-To:\&quot; header. | [optional] 
**sendAsEmail** | **String** | The email address that appears in the \&quot;From:\&quot; header for mail sent using this alias. This is read-only for all operations except create. | [optional] 
**signature** | **String** | An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only. | [optional] 
**smtpMsa** | [**SmtpMsa**](SmtpMsa.md) |  | [optional] 
**treatAsAlias** | **Boolean** | Whether Gmail should treat this address as an alias for the user&#39;s primary email address. This setting only applies to custom \&quot;from\&quot; aliases. | [optional] 
**verificationStatus** | **String** | Indicates whether this address has been verified for use as a send-as alias. Read-only. This setting only applies to custom \&quot;from\&quot; aliases. | [optional] 



## Enum: VerificationStatusEnum


* `verificationStatusUnspecified` (value: `"verificationStatusUnspecified"`)

* `accepted` (value: `"accepted"`)

* `pending` (value: `"pending"`)




