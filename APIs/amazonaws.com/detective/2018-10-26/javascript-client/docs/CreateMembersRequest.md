# AmazonDetective.CreateMembersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graphArn** | **String** | The ARN of the behavior graph. | 
**message** | **String** | Customized message text to include in the invitation email message to the invited member accounts. | [optional] 
**disableEmailNotification** | **Boolean** | &lt;p&gt;if set to &lt;code&gt;true&lt;/code&gt;, then the invited accounts do not receive email notifications. By default, this is set to &lt;code&gt;false&lt;/code&gt;, and the invited accounts receive email notifications.&lt;/p&gt; &lt;p&gt;Organization accounts in the organization behavior graph do not receive email notifications.&lt;/p&gt; | [optional] 
**accounts** | [**[Account]**](Account.md) | The list of Amazon Web Services accounts to invite or to enable. You can invite or enable up to 50 accounts at a time. For each invited account, the account list contains the account identifier and the Amazon Web Services account root user email address. For organization accounts in the organization behavior graph, the email address is not required. | 


