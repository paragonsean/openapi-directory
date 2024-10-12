

# PutEmailIdentityMailFromAttributesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mailFromDomain** | **String** | The domain to use as a MAIL FROM domain. |  [optional] |
|**behaviorOnMxFailure** | [**BehaviorOnMxFailureEnum**](#BehaviorOnMxFailureEnum) | &lt;p&gt;The action to take if the required MX record can&#39;t be found when you send an email. When you set this value to &lt;code&gt;UseDefaultValue&lt;/code&gt;, the mail is sent using &lt;i&gt;amazonses.com&lt;/i&gt; as the MAIL FROM domain. When you set this value to &lt;code&gt;RejectMessage&lt;/code&gt;, the Amazon SES API v2 returns a &lt;code&gt;MailFromDomainNotVerified&lt;/code&gt; error, and doesn&#39;t attempt to deliver the email.&lt;/p&gt; &lt;p&gt;These behaviors are taken when the custom MAIL FROM domain configuration is in the &lt;code&gt;Pending&lt;/code&gt;, &lt;code&gt;Failed&lt;/code&gt;, and &lt;code&gt;TemporaryFailure&lt;/code&gt; states.&lt;/p&gt; |  [optional] |



## Enum: BehaviorOnMxFailureEnum

| Name | Value |
|---- | -----|
| USE_DEFAULT_VALUE | &quot;USE_DEFAULT_VALUE&quot; |
| REJECT_MESSAGE | &quot;REJECT_MESSAGE&quot; |



