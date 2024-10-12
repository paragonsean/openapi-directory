

# CreateServiceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) | &lt;p&gt;The type of IAM policy.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NONE&lt;/code&gt;: The resource does not use an IAM policy. This is the default.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS_IAM&lt;/code&gt;: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**certificateArn** | **String** | The Amazon Resource Name (ARN) of the certificate. |  [optional] |
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren&#39;t identical, the retry fails. |  [optional] |
|**customDomainName** | **String** | The custom domain name of the service. |  [optional] |
|**name** | **String** | The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can&#39;t use a hyphen as the first or last character, or immediately after another hyphen. |  |
|**tags** | **Map&lt;String, String&gt;** | The tags for the service. |  [optional] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| AWS_IAM | &quot;AWS_IAM&quot; |



