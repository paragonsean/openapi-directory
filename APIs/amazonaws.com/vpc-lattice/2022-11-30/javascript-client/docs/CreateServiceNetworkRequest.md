# AmazonVpcLattice.CreateServiceNetworkRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authType** | **String** | &lt;p&gt;The type of IAM policy.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NONE&lt;/code&gt;: The resource does not use an IAM policy. This is the default.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS_IAM&lt;/code&gt;: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren&#39;t identical, the retry fails. | [optional] 
**name** | **String** | The name of the service network. The name must be unique to the account. The valid characters are a-z, 0-9, and hyphens (-). You can&#39;t use a hyphen as the first or last character, or immediately after another hyphen. | 
**tags** | **{String: String}** | The tags for the service network. | [optional] 



## Enum: AuthTypeEnum


* `NONE` (value: `"NONE"`)

* `AWS_IAM` (value: `"AWS_IAM"`)




