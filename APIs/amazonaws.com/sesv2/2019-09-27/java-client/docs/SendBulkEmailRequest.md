

# SendBulkEmailRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fromEmailAddress** | **String** | The email address to use as the \&quot;From\&quot; address for the email. The address that you specify has to be verified. |  [optional] |
|**fromEmailAddressIdentityArn** | **String** | &lt;p&gt;This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the &lt;code&gt;FromEmailAddress&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use sender@example.com, then you would specify the &lt;code&gt;FromEmailAddressIdentityArn&lt;/code&gt; to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the &lt;code&gt;FromEmailAddress&lt;/code&gt; to be sender@example.com.&lt;/p&gt; &lt;p&gt;For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**replyToAddresses** | **List&lt;String&gt;** | The \&quot;Reply-to\&quot; email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply. |  [optional] |
|**feedbackForwardingEmailAddress** | **String** | The address that you want bounce and complaint notifications to be sent to. |  [optional] |
|**feedbackForwardingEmailAddressIdentityArn** | **String** | &lt;p&gt;This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the &lt;code&gt;FeedbackForwardingEmailAddress&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the &lt;code&gt;FeedbackForwardingEmailAddressIdentityArn&lt;/code&gt; to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the &lt;code&gt;FeedbackForwardingEmailAddress&lt;/code&gt; to be feedback@example.com.&lt;/p&gt; &lt;p&gt;For more information about sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**defaultEmailTags** | [**List&lt;MessageTag&gt;**](MessageTag.md) | A list of message tags. |  [optional] |
|**defaultContent** | [**SendBulkEmailRequestDefaultContent**](SendBulkEmailRequestDefaultContent.md) |  |  |
|**bulkEmailEntries** | [**List&lt;BulkEmailEntry&gt;**](BulkEmailEntry.md) | A list of &lt;code&gt;BulkEmailEntry&lt;/code&gt; objects. |  |
|**configurationSetName** | **String** | &lt;p&gt;The name of a configuration set.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt; |  [optional] |



