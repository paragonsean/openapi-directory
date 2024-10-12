# AmazonSimpleEmailService.CreateCustomVerificationEmailTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templateName** | **String** | The name of the template. You will refer to this name when you send email using the &lt;code&gt;SendTemplatedEmail&lt;/code&gt; or &lt;code&gt;SendBulkTemplatedEmail&lt;/code&gt; operations. | 
**fromEmailAddress** | **String** | The email address that the custom verification email is sent from. | 
**templateSubject** | **String** | The subject line of the email. | 
**templateContent** | **String** | The content of the custom verification email template. | 
**successRedirectionURL** | **String** | The URL that the recipient of the verification email is sent to if his or her address is successfully verified. | 
**failureRedirectionURL** | **String** | The URL that the recipient of the verification email is sent to if his or her address is not successfully verified. | 


