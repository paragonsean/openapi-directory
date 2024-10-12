# AmazonOpenSearchService.UpdateDomainConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterConfig** | [**CreateDomainRequestClusterConfig**](CreateDomainRequestClusterConfig.md) |  | [optional] 
**eBSOptions** | [**CreateDomainRequestEBSOptions**](CreateDomainRequestEBSOptions.md) |  | [optional] 
**snapshotOptions** | [**CreateDomainRequestSnapshotOptions**](CreateDomainRequestSnapshotOptions.md) |  | [optional] 
**vPCOptions** | [**CreateDomainRequestVPCOptions**](CreateDomainRequestVPCOptions.md) |  | [optional] 
**cognitoOptions** | [**CreateDomainRequestCognitoOptions**](CreateDomainRequestCognitoOptions.md) |  | [optional] 
**advancedOptions** | **{String: String}** | &lt;p&gt;Exposes native OpenSearch configuration values from &lt;code&gt;opensearch.yml&lt;/code&gt;. The following advanced options are available: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Allows references to indexes in an HTTP request body. Must be &lt;code&gt;false&lt;/code&gt; when configuring access to individual sub-resources. Default is &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Specifies the percentage of heap space allocated to field data. Default is unbounded.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options\&quot;&gt;Advanced cluster parameters&lt;/a&gt;.&lt;/p&gt; | [optional] 
**accessPolicies** | **String** | Access policy rules for an Amazon OpenSearch Service domain endpoint. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-access-policies\&quot;&gt;Configuring access policies&lt;/a&gt;. The maximum size of a policy document is 100 KB. | [optional] 
**logPublishingOptions** | [**{String: LogPublishingOption}**](LogPublishingOption.md) | Options to publish OpenSearch logs to Amazon CloudWatch Logs. | [optional] 
**encryptionAtRestOptions** | [**CreateDomainRequestEncryptionAtRestOptions**](CreateDomainRequestEncryptionAtRestOptions.md) |  | [optional] 
**domainEndpointOptions** | [**CreateDomainRequestDomainEndpointOptions**](CreateDomainRequestDomainEndpointOptions.md) |  | [optional] 
**nodeToNodeEncryptionOptions** | [**CreateDomainRequestNodeToNodeEncryptionOptions**](CreateDomainRequestNodeToNodeEncryptionOptions.md) |  | [optional] 
**advancedSecurityOptions** | [**CreateDomainRequestAdvancedSecurityOptions**](CreateDomainRequestAdvancedSecurityOptions.md) |  | [optional] 
**autoTuneOptions** | [**UpdateDomainConfigRequestAutoTuneOptions**](UpdateDomainConfigRequestAutoTuneOptions.md) |  | [optional] 
**dryRun** | **Boolean** | This flag, when set to True, specifies whether the &lt;code&gt;UpdateDomain&lt;/code&gt; request should return the results of a dry run analysis without actually applying the change. A dry run determines what type of deployment the update will cause. | [optional] 
**dryRunMode** | **String** | &lt;p&gt;The type of dry run to perform.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Basic&lt;/code&gt; only returns the type of deployment (blue/green or dynamic) that the update will cause.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Verbose&lt;/code&gt; runs an additional check to validate the changes you&#39;re making. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#validation-check\&quot;&gt;Validating a domain update&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**offPeakWindowOptions** | [**CreateDomainRequestOffPeakWindowOptions**](CreateDomainRequestOffPeakWindowOptions.md) |  | [optional] 
**softwareUpdateOptions** | [**CreateDomainRequestSoftwareUpdateOptions**](CreateDomainRequestSoftwareUpdateOptions.md) |  | [optional] 



## Enum: DryRunModeEnum


* `Basic` (value: `"Basic"`)

* `Verbose` (value: `"Verbose"`)




