

# UpdateGraphqlApiRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The new name for the &lt;code&gt;GraphqlApi&lt;/code&gt; object. |  |
|**logConfig** | [**CreateGraphqlApiRequestLogConfig**](CreateGraphqlApiRequestLogConfig.md) |  |  [optional] |
|**authenticationType** | [**AuthenticationTypeEnum**](#AuthenticationTypeEnum) | The new authentication type for the &lt;code&gt;GraphqlApi&lt;/code&gt; object. |  [optional] |
|**userPoolConfig** | [**CreateGraphqlApiRequestUserPoolConfig**](CreateGraphqlApiRequestUserPoolConfig.md) |  |  [optional] |
|**openIDConnectConfig** | [**CreateGraphqlApiRequestOpenIDConnectConfig**](CreateGraphqlApiRequestOpenIDConnectConfig.md) |  |  [optional] |
|**additionalAuthenticationProviders** | [**List&lt;AdditionalAuthenticationProvider&gt;**](AdditionalAuthenticationProvider.md) | A list of additional authentication providers for the &lt;code&gt;GraphqlApi&lt;/code&gt; API. |  [optional] |
|**xrayEnabled** | **Boolean** | A flag indicating whether to use X-Ray tracing for the &lt;code&gt;GraphqlApi&lt;/code&gt;. |  [optional] |
|**lambdaAuthorizerConfig** | [**CreateGraphqlApiRequestLambdaAuthorizerConfig**](CreateGraphqlApiRequestLambdaAuthorizerConfig.md) |  |  [optional] |
|**mergedApiExecutionRoleArn** | **String** | The Identity and Access Management service role ARN for a merged API. The AppSync service assumes this role on behalf of the Merged API to validate access to source APIs at runtime and to prompt the &lt;code&gt;AUTO_MERGE&lt;/code&gt; to update the merged API endpoint with the source API changes automatically. |  [optional] |
|**ownerContact** | **String** | &lt;p&gt;The owner contact information for an API resource.&lt;/p&gt; &lt;p&gt;This field accepts any string input with a length of 0 - 256 characters.&lt;/p&gt; |  [optional] |



## Enum: AuthenticationTypeEnum

| Name | Value |
|---- | -----|
| API_KEY | &quot;API_KEY&quot; |
| AWS_IAM | &quot;AWS_IAM&quot; |
| AMAZON_COGNITO_USER_POOLS | &quot;AMAZON_COGNITO_USER_POOLS&quot; |
| OPENID_CONNECT | &quot;OPENID_CONNECT&quot; |
| AWS_LAMBDA | &quot;AWS_LAMBDA&quot; |



