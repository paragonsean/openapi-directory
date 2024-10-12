

# CreateInvitationsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountIds** | **List&lt;String&gt;** | An array that lists Amazon Web Services account IDs, one for each account to send the invitation to. |  |
|**disableEmailNotification** | **Boolean** | Specifies whether to send the invitation as an email message. If this value is false, Amazon Macie sends the invitation (as an email message) to the email address that you specified for the recipient&#39;s account when you associated the account with your account. The default value is false. |  [optional] |
|**message** | **String** | Custom text to include in the email message that contains the invitation. The text can contain as many as 80 alphanumeric characters. |  [optional] |



