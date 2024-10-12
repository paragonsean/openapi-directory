

# UpdateElasticsearchDomainConfigRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**elasticsearchClusterConfig** | [**CreateElasticsearchDomainRequestElasticsearchClusterConfig**](CreateElasticsearchDomainRequestElasticsearchClusterConfig.md) |  |  [optional] |
|**ebSOptions** | [**CreateElasticsearchDomainRequestEBSOptions**](CreateElasticsearchDomainRequestEBSOptions.md) |  |  [optional] |
|**snapshotOptions** | [**CreateElasticsearchDomainRequestSnapshotOptions**](CreateElasticsearchDomainRequestSnapshotOptions.md) |  |  [optional] |
|**vpCOptions** | [**CreateElasticsearchDomainRequestVPCOptions**](CreateElasticsearchDomainRequestVPCOptions.md) |  |  [optional] |
|**cognitoOptions** | [**CreateElasticsearchDomainRequestCognitoOptions**](CreateElasticsearchDomainRequestCognitoOptions.md) |  |  [optional] |
|**advancedOptions** | **Map&lt;String, String&gt;** | &lt;p&gt; Exposes select native Elasticsearch configuration values from &lt;code&gt;elasticsearch.yml&lt;/code&gt;. Currently, the following advanced options are available:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;Option to allow references to indices in an HTTP request body. Must be &lt;code&gt;false&lt;/code&gt; when configuring access to individual sub-resources. By default, the value is &lt;code&gt;true&lt;/code&gt;. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuration Advanced Options&lt;/a&gt; for more information.&lt;/li&gt; &lt;li&gt;Option to specify the percentage of heap space that is allocated to field data. By default, this setting is unbounded.&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options\&quot;&gt;Configuring Advanced Options&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**accessPolicies** | **String** | Access policy rules for an Elasticsearch domain service endpoints. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Access Policies&lt;/a&gt; in the &lt;i&gt;Amazon Elasticsearch Service Developer Guide&lt;/i&gt;. The maximum size of a policy document is 100 KB. |  [optional] |
|**logPublishingOptions** | [**Map&lt;String, LogPublishingOption&gt;**](LogPublishingOption.md) | Map of &lt;code&gt;LogType&lt;/code&gt; and &lt;code&gt;LogPublishingOption&lt;/code&gt;, each containing options to publish a given type of Elasticsearch log. |  [optional] |
|**domainEndpointOptions** | [**CreateElasticsearchDomainRequestDomainEndpointOptions**](CreateElasticsearchDomainRequestDomainEndpointOptions.md) |  |  [optional] |
|**advancedSecurityOptions** | [**CreateElasticsearchDomainRequestAdvancedSecurityOptions**](CreateElasticsearchDomainRequestAdvancedSecurityOptions.md) |  |  [optional] |
|**nodeToNodeEncryptionOptions** | [**CreateElasticsearchDomainRequestNodeToNodeEncryptionOptions**](CreateElasticsearchDomainRequestNodeToNodeEncryptionOptions.md) |  |  [optional] |
|**encryptionAtRestOptions** | [**CreateElasticsearchDomainRequestEncryptionAtRestOptions**](CreateElasticsearchDomainRequestEncryptionAtRestOptions.md) |  |  [optional] |
|**autoTuneOptions** | [**UpdateElasticsearchDomainConfigRequestAutoTuneOptions**](UpdateElasticsearchDomainConfigRequestAutoTuneOptions.md) |  |  [optional] |
|**dryRun** | **Boolean** |  This flag, when set to True, specifies whether the &lt;code&gt;UpdateElasticsearchDomain&lt;/code&gt; request should return the results of validation checks without actually applying the change. This flag, when set to True, specifies the deployment mechanism through which the update shall be applied on the domain. This will not actually perform the Update.  |  [optional] |



