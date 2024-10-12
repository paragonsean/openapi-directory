# AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alwaysOn** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if Always On is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**apiDefinition** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigApiDefinition**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigApiDefinition.md) |  | [optional] 
**appCommandLine** | **String** | App command line to launch. | [optional] 
**appSettings** | [**[AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAppSettingsInner]**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAppSettingsInner.md) | Application settings. | [optional] 
**autoHealEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if Auto Heal is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**autoHealRules** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules.md) |  | [optional] 
**autoSwapSlotName** | **String** | Auto-swap slot name. | [optional] 
**connectionStrings** | [**[AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner]**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner.md) | Connection strings. | [optional] 
**cors** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigCors**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigCors.md) |  | [optional] 
**defaultDocuments** | **[String]** | Default documents. | [optional] 
**detailedErrorLoggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if detailed error logging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**documentRoot** | **String** | Document root. | [optional] 
**experiments** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments.md) |  | [optional] 
**handlerMappings** | [**[AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigHandlerMappingsInner]**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigHandlerMappingsInner.md) | Handler mappings. | [optional] 
**http20Enabled** | **Boolean** | Http20Enabled: configures a web site to allow clients to connect over http2.0 | [optional] [default to true]
**httpLoggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if HTTP logging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**ipSecurityRestrictions** | [**[AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner]**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.md) | IP security restrictions. | [optional] 
**javaContainer** | **String** | Java container. | [optional] 
**javaContainerVersion** | **String** | Java container version. | [optional] 
**javaVersion** | **String** | Java version. | [optional] 
**limits** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.md) |  | [optional] 
**linuxFxVersion** | **String** | Linux App Framework and version | [optional] 
**loadBalancing** | **String** | Site load balancing. | [optional] 
**localMySqlEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to enable local MySQL; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] [default to false]
**logsDirectorySizeLimit** | **Number** | HTTP logs directory size limit. | [optional] 
**machineKey** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey.md) |  | [optional] 
**managedPipelineMode** | **String** | Managed pipeline mode. | [optional] 
**minTlsVersion** | **String** | MinTlsVersion: configures the minimum version of TLS required for SSL requests | [optional] 
**netFrameworkVersion** | **String** | .NET Framework version. | [optional] [default to &#39;v4.6&#39;]
**nodeVersion** | **String** | Version of Node.js. | [optional] 
**numberOfWorkers** | **Number** | Number of workers. | [optional] 
**phpVersion** | **String** | Version of PHP. | [optional] 
**publishingUsername** | **String** | Publishing user name. | [optional] 
**push** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush.md) |  | [optional] 
**pythonVersion** | **String** | Version of Python. | [optional] 
**remoteDebuggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if remote debugging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**remoteDebuggingVersion** | **String** | Remote debugging version. | [optional] 
**requestTracingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if request tracing is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**requestTracingExpirationTime** | **Date** | Request tracing expiration time. | [optional] 
**scmType** | **String** | SCM type. | [optional] 
**tracingOptions** | **String** | Tracing options. | [optional] 
**use32BitWorkerProcess** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to use 32-bit worker process; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**virtualApplications** | [**[AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInner]**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInner.md) | Virtual applications. | [optional] 
**vnetName** | **String** | Virtual Network name. | [optional] 
**webSocketsEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if WebSocket is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 



## Enum: LoadBalancingEnum


* `WeightedRoundRobin` (value: `"WeightedRoundRobin"`)

* `LeastRequests` (value: `"LeastRequests"`)

* `LeastResponseTime` (value: `"LeastResponseTime"`)

* `WeightedTotalTraffic` (value: `"WeightedTotalTraffic"`)

* `RequestHash` (value: `"RequestHash"`)





## Enum: ManagedPipelineModeEnum


* `Integrated` (value: `"Integrated"`)

* `Classic` (value: `"Classic"`)





## Enum: MinTlsVersionEnum


* `0` (value: `"1.0"`)

* `1` (value: `"1.1"`)

* `2` (value: `"1.2"`)





## Enum: ScmTypeEnum


* `None` (value: `"None"`)

* `Dropbox` (value: `"Dropbox"`)

* `Tfs` (value: `"Tfs"`)

* `LocalGit` (value: `"LocalGit"`)

* `GitHub` (value: `"GitHub"`)

* `CodePlexGit` (value: `"CodePlexGit"`)

* `CodePlexHg` (value: `"CodePlexHg"`)

* `BitbucketGit` (value: `"BitbucketGit"`)

* `BitbucketHg` (value: `"BitbucketHg"`)

* `ExternalGit` (value: `"ExternalGit"`)

* `ExternalHg` (value: `"ExternalHg"`)

* `OneDrive` (value: `"OneDrive"`)

* `VSO` (value: `"VSO"`)




