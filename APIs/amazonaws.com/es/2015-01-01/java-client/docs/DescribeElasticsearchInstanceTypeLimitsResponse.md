

# DescribeElasticsearchInstanceTypeLimitsResponse

 Container for the parameters received from <code> <a>DescribeElasticsearchInstanceTypeLimits</a> </code> operation. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**limitsByRole** | [**Map&lt;String, Limits&gt;**](Limits.md) |  Map of Role of the Instance and Limits that are applicable. Role performed by given Instance in Elasticsearch can be one of the following: &lt;ul&gt; &lt;li&gt;data: If the given InstanceType is used as data node&lt;/li&gt; &lt;li&gt;master: If the given InstanceType is used as master node&lt;/li&gt; &lt;li&gt;ultra_warm: If the given InstanceType is used as warm node&lt;/li&gt; &lt;/ul&gt;  |  [optional] |



