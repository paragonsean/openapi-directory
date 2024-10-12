# AmazonOpenSearchService.UpgradeDomainRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainName** | **String** | The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an Amazon Web Services Region. | 
**targetVersion** | **String** | OpenSearch or Elasticsearch version to which you want to upgrade, in the format Opensearch_X.Y or Elasticsearch_X.Y. | 
**performCheckOnly** | **Boolean** | When true, indicates that an upgrade eligibility check needs to be performed. Does not actually perform the upgrade. | [optional] 
**advancedOptions** | **{String: String}** | &lt;p&gt;Exposes native OpenSearch configuration values from &lt;code&gt;opensearch.yml&lt;/code&gt;. The following advanced options are available: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Allows references to indexes in an HTTP request body. Must be &lt;code&gt;false&lt;/code&gt; when configuring access to individual sub-resources. Default is &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specifies the percentage of heap space allocated to field data. Default is unbounded.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options\&quot;&gt;Advanced cluster parameters&lt;/a&gt;.&lt;/p&gt; | [optional] 


