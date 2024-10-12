

# UpdateServiceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) | &lt;p&gt;The type of IAM policy.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NONE&lt;/code&gt;: The resource does not use an IAM policy. This is the default.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS_IAM&lt;/code&gt;: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**certificateArn** | **String** | The Amazon Resource Name (ARN) of the certificate.  |  [optional] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| AWS_IAM | &quot;AWS_IAM&quot; |



