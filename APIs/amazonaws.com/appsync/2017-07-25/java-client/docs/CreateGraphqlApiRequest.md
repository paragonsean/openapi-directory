

# CreateGraphqlApiRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | A user-supplied name for the &lt;code&gt;GraphqlApi&lt;/code&gt;. |  |
|**logConfig** | [**CreateGraphqlApiRequestLogConfig**](CreateGraphqlApiRequestLogConfig.md) |  |  [optional] |
|**authenticationType** | [**AuthenticationTypeEnum**](#AuthenticationTypeEnum) | The authentication type: API key, Identity and Access Management (IAM), OpenID Connect (OIDC), Amazon Cognito user pools, or Lambda. |  |
|**userPoolConfig** | [**CreateGraphqlApiRequestUserPoolConfig**](CreateGraphqlApiRequestUserPoolConfig.md) |  |  [optional] |
|**openIDConnectConfig** | [**CreateGraphqlApiRequestOpenIDConnectConfig**](CreateGraphqlApiRequestOpenIDConnectConfig.md) |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A map with keys of &lt;code&gt;TagKey&lt;/code&gt; objects and values of &lt;code&gt;TagValue&lt;/code&gt; objects. |  [optional] |
|**additionalAuthenticationProviders** | [**List&lt;AdditionalAuthenticationProvider&gt;**](AdditionalAuthenticationProvider.md) | A list of additional authentication providers for the &lt;code&gt;GraphqlApi&lt;/code&gt; API. |  [optional] |
|**xrayEnabled** | **Boolean** | A flag indicating whether to use X-Ray tracing for the &lt;code&gt;GraphqlApi&lt;/code&gt;. |  [optional] |
|**lambdaAuthorizerConfig** | [**CreateGraphqlApiRequestLambdaAuthorizerConfig**](CreateGraphqlApiRequestLambdaAuthorizerConfig.md) |  |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | Sets the value of the GraphQL API to public (&lt;code&gt;GLOBAL&lt;/code&gt;) or private (&lt;code&gt;PRIVATE&lt;/code&gt;). If no value is provided, the visibility will be set to &lt;code&gt;GLOBAL&lt;/code&gt; by default. This value cannot be changed once the API has been created. |  [optional] |
|**apiType** | [**ApiTypeEnum**](#ApiTypeEnum) | The value that indicates whether the GraphQL API is a standard API (&lt;code&gt;GRAPHQL&lt;/code&gt;) or merged API (&lt;code&gt;MERGED&lt;/code&gt;). |  [optional] |
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



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| GLOBAL | &quot;GLOBAL&quot; |
| PRIVATE | &quot;PRIVATE&quot; |



## Enum: ApiTypeEnum

| Name | Value |
|---- | -----|
| GRAPHQL | &quot;GRAPHQL&quot; |
| MERGED | &quot;MERGED&quot; |



