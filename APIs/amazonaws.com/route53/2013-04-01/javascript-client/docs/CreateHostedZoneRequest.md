# AmazonRoute53.CreateHostedZoneRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | &lt;p&gt;The name of the domain. Specify a fully qualified domain name, for example, &lt;i&gt;www.example.com&lt;/i&gt;. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats &lt;i&gt;www.example.com&lt;/i&gt; (without a trailing dot) and &lt;i&gt;www.example.com.&lt;/i&gt; (with a trailing dot) as identical.&lt;/p&gt; &lt;p&gt;If you&#39;re creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of &lt;code&gt;NameServers&lt;/code&gt; that &lt;code&gt;CreateHostedZone&lt;/code&gt; returns in &lt;code&gt;DelegationSet&lt;/code&gt;.&lt;/p&gt; | 
**VPC** | [**AssociateVPCWithHostedZoneRequestVPC**](AssociateVPCWithHostedZoneRequestVPC.md) |  | [optional] 
**callerReference** | **String** | A unique string that identifies the request and that allows failed &lt;code&gt;CreateHostedZone&lt;/code&gt; requests to be retried without the risk of executing the operation twice. You must use a unique &lt;code&gt;CallerReference&lt;/code&gt; string every time you submit a &lt;code&gt;CreateHostedZone&lt;/code&gt; request. &lt;code&gt;CallerReference&lt;/code&gt; can be any unique string, for example, a date/time stamp. | 
**hostedZoneConfig** | [**CreateHostedZoneRequestHostedZoneConfig**](CreateHostedZoneRequestHostedZoneConfig.md) |  | [optional] 
**delegationSetId** | **String** | &lt;p&gt;If you want to associate a reusable delegation set with this hosted zone, the ID that Amazon Route 53 assigned to the reusable delegation set when you created it. For more information about reusable delegation sets, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateReusableDelegationSet.html\&quot;&gt;CreateReusableDelegationSet&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you are using a reusable delegation set to create a public hosted zone for a subdomain, make sure that the parent hosted zone doesn&#39;t use one or more of the same name servers. If you have overlapping nameservers, the operation will cause a &lt;code&gt;ConflictingDomainsExist&lt;/code&gt; error.&lt;/p&gt; | [optional] 


