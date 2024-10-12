

# SendCustomVerificationEmailRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailAddress** | **String** | The email address to verify. |  |
|**templateName** | **String** | The name of the template. You will refer to this name when you send email using the &lt;code&gt;SendTemplatedEmail&lt;/code&gt; or &lt;code&gt;SendBulkTemplatedEmail&lt;/code&gt; operations. |  |
|**configurationSetName** | **String** | &lt;p&gt;The name of a configuration set.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt; |  [optional] |



