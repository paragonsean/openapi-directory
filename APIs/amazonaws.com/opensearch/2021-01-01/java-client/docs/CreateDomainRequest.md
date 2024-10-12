

# CreateDomainRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainName** | **String** | The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an Amazon Web Services Region. |  |
|**engineVersion** | **String** | String of format Elasticsearch_X.Y or OpenSearch_X.Y to specify the engine version for the OpenSearch Service domain. For example, &lt;code&gt;OpenSearch_1.0&lt;/code&gt; or &lt;code&gt;Elasticsearch_7.9&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomains\&quot;&gt;Creating and managing Amazon OpenSearch Service domains&lt;/a&gt;. |  [optional] |
|**clusterConfig** | [**CreateDomainRequestClusterConfig**](CreateDomainRequestClusterConfig.md) |  |  [optional] |
|**ebSOptions** | [**CreateDomainRequestEBSOptions**](CreateDomainRequestEBSOptions.md) |  |  [optional] |
|**accessPolicies** | **String** | Access policy rules for an Amazon OpenSearch Service domain endpoint. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-access-policies\&quot;&gt;Configuring access policies&lt;/a&gt;. The maximum size of a policy document is 100 KB. |  [optional] |
|**snapshotOptions** | [**CreateDomainRequestSnapshotOptions**](CreateDomainRequestSnapshotOptions.md) |  |  [optional] |
|**vpCOptions** | [**CreateDomainRequestVPCOptions**](CreateDomainRequestVPCOptions.md) |  |  [optional] |
|**cognitoOptions** | [**CreateDomainRequestCognitoOptions**](CreateDomainRequestCognitoOptions.md) |  |  [optional] |
|**encryptionAtRestOptions** | [**CreateDomainRequestEncryptionAtRestOptions**](CreateDomainRequestEncryptionAtRestOptions.md) |  |  [optional] |
|**nodeToNodeEncryptionOptions** | [**CreateDomainRequestNodeToNodeEncryptionOptions**](CreateDomainRequestNodeToNodeEncryptionOptions.md) |  |  [optional] |
|**advancedOptions** | **Map&lt;String, String&gt;** | &lt;p&gt;Exposes native OpenSearch configuration values from &lt;code&gt;opensearch.yml&lt;/code&gt;. The following advanced options are available: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Allows references to indexes in an HTTP request body. Must be &lt;code&gt;false&lt;/code&gt; when configuring access to individual sub-resources. Default is &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specifies the percentage of heap space allocated to field data. Default is unbounded.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options\&quot;&gt;Advanced cluster parameters&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**logPublishingOptions** | [**Map&lt;String, LogPublishingOption&gt;**](LogPublishingOption.md) | Key-value pairs to configure log publishing. |  [optional] |
|**domainEndpointOptions** | [**CreateDomainRequestDomainEndpointOptions**](CreateDomainRequestDomainEndpointOptions.md) |  |  [optional] |
|**advancedSecurityOptions** | [**CreateDomainRequestAdvancedSecurityOptions**](CreateDomainRequestAdvancedSecurityOptions.md) |  |  [optional] |
|**tagList** | [**List&lt;Tag&gt;**](Tag.md) | A list of tags attached to a domain. |  [optional] |
|**autoTuneOptions** | [**CreateDomainRequestAutoTuneOptions**](CreateDomainRequestAutoTuneOptions.md) |  |  [optional] |
|**offPeakWindowOptions** | [**CreateDomainRequestOffPeakWindowOptions**](CreateDomainRequestOffPeakWindowOptions.md) |  |  [optional] |
|**softwareUpdateOptions** | [**CreateDomainRequestSoftwareUpdateOptions**](CreateDomainRequestSoftwareUpdateOptions.md) |  |  [optional] |



