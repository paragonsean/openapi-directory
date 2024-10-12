

# DescribeInboundCrossClusterSearchConnectionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filters** | [**List&lt;Filter&gt;**](Filter.md) |  A list of filters used to match properties for inbound cross-cluster search connection. Available &lt;code&gt;&lt;a&gt;Filter&lt;/a&gt;&lt;/code&gt; names for this operation are: &lt;ul&gt; &lt;li&gt;cross-cluster-search-connection-id&lt;/li&gt; &lt;li&gt;source-domain-info.domain-name&lt;/li&gt; &lt;li&gt;source-domain-info.owner-id&lt;/li&gt; &lt;li&gt;source-domain-info.region&lt;/li&gt; &lt;li&gt;destination-domain-info.domain-name&lt;/li&gt; &lt;/ul&gt;  |  [optional] |
|**maxResults** | **Integer** |  Set this value to limit the number of results returned.  |  [optional] |
|**nextToken** | **String** |  Paginated APIs accepts NextToken input to returns next page results and provides a NextToken output in the response which can be used by the client to retrieve more results.  |  [optional] |



