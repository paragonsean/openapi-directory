# AmazonSimpleEmailService.PutEmailIdentityDkimSigningAttributesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signingAttributesOrigin** | **String** | &lt;p&gt;The method to use to configure DKIM for the identity. There are the following possible values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS_SES&lt;/code&gt; – Configure DKIM for the identity by using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html\&quot;&gt;Easy DKIM&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;EXTERNAL&lt;/code&gt; – Configure DKIM for the identity by using Bring Your Own DKIM (BYODKIM).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**signingAttributes** | [**CreateEmailIdentityRequestDkimSigningAttributes**](CreateEmailIdentityRequestDkimSigningAttributes.md) |  | [optional] 



## Enum: SigningAttributesOriginEnum


* `AWS_SES` (value: `"AWS_SES"`)

* `EXTERNAL` (value: `"EXTERNAL"`)




