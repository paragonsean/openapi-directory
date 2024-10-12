# AmazonPinpointEmailService.PutEmailIdentityMailFromAttributesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailFromDomain** | **String** | The domain that you want to use as a MAIL FROM domain. | [optional] 
**behaviorOnMxFailure** | **String** | &lt;p&gt;The action that you want Amazon Pinpoint to take if it can&#39;t read the required MX record for a custom MAIL FROM domain. When you set this value to &lt;code&gt;UseDefaultValue&lt;/code&gt;, Amazon Pinpoint uses &lt;i&gt;amazonses.com&lt;/i&gt; as the MAIL FROM domain. When you set this value to &lt;code&gt;RejectMessage&lt;/code&gt;, Amazon Pinpoint returns a &lt;code&gt;MailFromDomainNotVerified&lt;/code&gt; error, and doesn&#39;t attempt to deliver the email.&lt;/p&gt; &lt;p&gt;These behaviors are taken when the custom MAIL FROM domain configuration is in the &lt;code&gt;Pending&lt;/code&gt;, &lt;code&gt;Failed&lt;/code&gt;, and &lt;code&gt;TemporaryFailure&lt;/code&gt; states.&lt;/p&gt; | [optional] 



## Enum: BehaviorOnMxFailureEnum


* `USE_DEFAULT_VALUE` (value: `"USE_DEFAULT_VALUE"`)

* `REJECT_MESSAGE` (value: `"REJECT_MESSAGE"`)




