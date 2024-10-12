# CodeArtifact.CreateDomainRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionKey** | **String** | &lt;p&gt; The encryption key for the domain. This is used to encrypt content stored in a domain. An encryption key can be a key ID, a key Amazon Resource Name (ARN), a key alias, or a key alias ARN. To specify an &lt;code&gt;encryptionKey&lt;/code&gt;, your IAM role must have &lt;code&gt;kms:DescribeKey&lt;/code&gt; and &lt;code&gt;kms:CreateGrant&lt;/code&gt; permissions on the encryption key that is used. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestSyntax\&quot;&gt;DescribeKey&lt;/a&gt; in the &lt;i&gt;Key Management Service API Reference&lt;/i&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html\&quot;&gt;Key Management Service API Permissions Reference&lt;/a&gt; in the &lt;i&gt;Key Management Service Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; CodeArtifact supports only symmetric CMKs. Do not associate an asymmetric CMK with your domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html\&quot;&gt;Using symmetric and asymmetric keys&lt;/a&gt; in the &lt;i&gt;Key Management Service Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;/important&gt; | [optional] 
**tags** | [**[Tag]**](Tag.md) | One or more tag key-value pairs for the domain. | [optional] 


