

# ResendTokenRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tokenType** | [**TokenTypeEnum**](#TokenTypeEnum) | The type of the token to resend |  |
|**verificationCode** | **String** | &lt;p&gt;Optional property that MUST be suppied when manually verifying a user&lt;/p&gt; &lt;p&gt;The user&#39;s smsNumber is registered via a separate endpoint and an OTP sent to them&lt;/p&gt;  |  [optional] |



## Enum: TokenTypeEnum

| Name | Value |
|---- | -----|
| INVITE_MFA_USER | &quot;INVITE_MFA_USER&quot; |
| MFA_REGISTRATION | &quot;MFA_REGISTRATION&quot; |



