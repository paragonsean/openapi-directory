# AmazonCloudSearch.AccessPoliciesStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | **String** | &lt;p&gt;An IAM access policy as described in &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?AccessPolicyLanguage.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;The Access Policy Language&lt;/a&gt; in &lt;i&gt;Using AWS Identity and Access Management&lt;/i&gt;. The maximum size of an access policy document is 100 KB.&lt;/p&gt; &lt;p&gt;Example: &lt;code&gt;{\&quot;Statement\&quot;: [{\&quot;Effect\&quot;:\&quot;Allow\&quot;, \&quot;Action\&quot;: \&quot;*\&quot;, \&quot;Resource\&quot;: \&quot;arn:aws:cs:us-east-1:1234567890:search/movies\&quot;, \&quot;Condition\&quot;: { \&quot;IpAddress\&quot;: { \&quot;aws:SourceIp\&quot;: [\&quot;203.0.113.1/32\&quot;] } }}, {\&quot;Effect\&quot;:\&quot;Allow\&quot;, \&quot;Action\&quot;: \&quot;*\&quot;, \&quot;Resource\&quot;: \&quot;arn:aws:cs:us-east-1:1234567890:documents/movies\&quot;, \&quot;Condition\&quot;: { \&quot;IpAddress\&quot;: { \&quot;aws:SourceIp\&quot;: [\&quot;203.0.113.1/32\&quot;] } }} ] }&lt;/code&gt;&lt;/p&gt; | 
**status** | [**OptionStatus**](OptionStatus.md) |  | 


