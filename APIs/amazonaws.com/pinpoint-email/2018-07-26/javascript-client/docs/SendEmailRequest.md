# AmazonPinpointEmailService.SendEmailRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fromEmailAddress** | **String** | The email address that you want to use as the \&quot;From\&quot; address for the email. The address that you specify has to be verified.  | [optional] 
**destination** | [**SendEmailRequestDestination**](SendEmailRequestDestination.md) |  | 
**replyToAddresses** | **[String]** | The \&quot;Reply-to\&quot; email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply. | [optional] 
**feedbackForwardingEmailAddress** | **String** | The address that Amazon Pinpoint should send bounce and complaint notifications to. | [optional] 
**content** | [**CreateDeliverabilityTestReportRequestContent**](CreateDeliverabilityTestReportRequestContent.md) |  | 
**emailTags** | [**[MessageTag]**](MessageTag.md) | A list of message tags. | [optional] 
**configurationSetName** | **String** | &lt;p&gt;The name of a configuration set.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt; | [optional] 


