# AmazonOpenSearchService.CreateOutboundConnectionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**localDomainInfo** | [**CreateOutboundConnectionRequestLocalDomainInfo**](CreateOutboundConnectionRequestLocalDomainInfo.md) |  | 
**remoteDomainInfo** | [**CreateOutboundConnectionRequestLocalDomainInfo**](CreateOutboundConnectionRequestLocalDomainInfo.md) |  | 
**connectionAlias** | **String** | Name of the connection. | 
**connectionMode** | **String** | &lt;p&gt;The connection mode for the cross-cluster connection.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;DIRECT&lt;/b&gt; - Used for cross-cluster search or cross-cluster replication.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;VPC_ENDPOINT&lt;/b&gt; - Used for remote reindex between Amazon OpenSearch Service VPC domains.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**connectionProperties** | [**CreateOutboundConnectionRequestConnectionProperties**](CreateOutboundConnectionRequestConnectionProperties.md) |  | [optional] 



## Enum: ConnectionModeEnum


* `DIRECT` (value: `"DIRECT"`)

* `VPC_ENDPOINT` (value: `"VPC_ENDPOINT"`)




