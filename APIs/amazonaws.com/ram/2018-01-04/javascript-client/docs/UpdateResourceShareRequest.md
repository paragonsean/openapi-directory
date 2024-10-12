# AwsResourceAccessManager.UpdateResourceShareRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceShareArn** | **String** | Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the resource share that you want to modify. | 
**name** | **String** | If specified, the new name that you want to attach to the resource share. | [optional] 
**allowExternalPrincipals** | **Boolean** | Specifies whether principals outside your organization in Organizations can be associated with a resource share. | [optional] 
**clientToken** | **String** | &lt;p&gt;Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a &lt;a href&#x3D;\&quot;https://wikipedia.org/wiki/Universally_unique_identifier\&quot;&gt;UUID type of value.&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t provide this value, then Amazon Web Services generates a random one for you.&lt;/p&gt; &lt;p&gt;If you retry the operation with the same &lt;code&gt;ClientToken&lt;/code&gt;, but with different parameters, the retry fails with an &lt;code&gt;IdempotentParameterMismatch&lt;/code&gt; error.&lt;/p&gt; | [optional] 


