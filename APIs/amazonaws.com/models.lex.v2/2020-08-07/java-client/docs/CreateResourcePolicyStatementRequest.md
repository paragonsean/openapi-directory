

# CreateResourcePolicyStatementRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**statementId** | **String** | The name of the statement. The ID is the same as the &lt;code&gt;Sid&lt;/code&gt; IAM property. The statement name must be unique within the policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_sid.html\&quot;&gt;IAM JSON policy elements: Sid&lt;/a&gt;.  |  |
|**effect** | [**EffectEnum**](#EffectEnum) | Determines whether the statement allows or denies access to the resource. |  |
|**principal** | [**List&lt;Principal&gt;**](Principal.md) | An IAM principal, such as an IAM user, IAM role, or Amazon Web Services services that is allowed or denied access to a resource. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html\&quot;&gt;Amazon Web Services JSON policy elements: Principal&lt;/a&gt;. |  |
|**action** | **List&lt;String&gt;** | The Amazon Lex action that this policy either allows or denies. The action must apply to the resource type of the specified ARN. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlexv2.html\&quot;&gt; Actions, resources, and condition keys for Amazon Lex V2&lt;/a&gt;. |  |
|**condition** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | &lt;p&gt;Specifies a condition when the policy is in effect. If the principal of the policy is a service principal, you must provide two condition blocks, one with a SourceAccount global condition key and one with a SourceArn global condition key.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html\&quot;&gt;IAM JSON policy elements: Condition &lt;/a&gt;.&lt;/p&gt; |  [optional] |



## Enum: EffectEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |
| DENY | &quot;Deny&quot; |



