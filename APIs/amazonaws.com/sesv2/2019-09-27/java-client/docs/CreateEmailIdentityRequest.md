

# CreateEmailIdentityRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailIdentity** | **String** | The email address or domain to verify. |  |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | An array of objects that define the tags (keys and values) to associate with the email identity. |  [optional] |
|**dkimSigningAttributes** | [**CreateEmailIdentityRequestDkimSigningAttributes**](CreateEmailIdentityRequestDkimSigningAttributes.md) |  |  [optional] |
|**configurationSetName** | **String** | &lt;p&gt;The name of a configuration set.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt; |  [optional] |



