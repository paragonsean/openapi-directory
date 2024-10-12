# AmazonRoute53.CreateKeySigningKeyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callerReference** | **String** | A unique string that identifies the request. | 
**hostedZoneId** | **String** | The unique string (ID) used to identify a hosted zone. | 
**keyManagementServiceArn** | **String** | &lt;p&gt;The Amazon resource name (ARN) for a customer managed key in Key Management Service (KMS). The &lt;code&gt;KeyManagementServiceArn&lt;/code&gt; must be unique for each key-signing key (KSK) in a single hosted zone. To see an example of &lt;code&gt;KeyManagementServiceArn&lt;/code&gt; that grants the correct permissions for DNSSEC, scroll down to &lt;b&gt;Example&lt;/b&gt;. &lt;/p&gt; &lt;p&gt;You must configure the customer managed customer managed key as follows:&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;Status&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Enabled&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Key spec&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;ECC_NIST_P256&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Key usage&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Sign and verify&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Key policy&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The key policy must give permission for the following actions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;DescribeKey&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;GetPublicKey&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Sign&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The key policy must also include the Amazon Route 53 service in the principal for your account. Specify the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;\&quot;Service\&quot;: \&quot;dnssec-route53.amazonaws.com\&quot;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/dd&gt; &lt;/dl&gt; &lt;p&gt;For more information about working with a customer managed key in KMS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html\&quot;&gt;Key Management Service concepts&lt;/a&gt;.&lt;/p&gt; | 
**name** | **String** | A string used to identify a key-signing key (KSK). &lt;code&gt;Name&lt;/code&gt; can include numbers, letters, and underscores (_). &lt;code&gt;Name&lt;/code&gt; must be unique for each key-signing key in the same hosted zone. | 
**status** | **String** | A string specifying the initial status of the key-signing key (KSK). You can set the value to &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;INACTIVE&lt;/code&gt;. | 


