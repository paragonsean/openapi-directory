# AppServiceEnvironmentsApiClient.AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alwaysOn** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if Always On is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**apiDefinition** | [**AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigApiDefinition**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigApiDefinition.md) |  | [optional] 
**apiManagementConfig** | [**AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigApiManagementConfig**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigApiManagementConfig.md) |  | [optional] 
**appCommandLine** | **String** | App command line to launch. | [optional] 
**appSettings** | [**[AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigAppSettingsInner]**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigAppSettingsInner.md) | Application settings. | [optional] 
**autoHealEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if Auto Heal is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**autoHealRules** | [**AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigAutoHealRules**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigAutoHealRules.md) |  | [optional] 
**autoSwapSlotName** | **String** | Auto-swap slot name. | [optional] 
**connectionStrings** | [**[AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner]**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner.md) | Connection strings. | [optional] 
**cors** | [**AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigCors**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigCors.md) |  | [optional] 
**defaultDocuments** | **[String]** | Default documents. | [optional] 
**detailedErrorLoggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if detailed error logging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**documentRoot** | **String** | Document root. | [optional] 
**experiments** | [**AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigExperiments**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigExperiments.md) |  | [optional] 
**ftpsState** | **String** | State of FTP / FTPS service | [optional] 
**handlerMappings** | [**[AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigHandlerMappingsInner]**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigHandlerMappingsInner.md) | Handler mappings. | [optional] 
**healthCheckPath** | **String** | Health check path | [optional] 
**http20Enabled** | **Boolean** | Http20Enabled: configures a web site to allow clients to connect over http2.0 | [optional] [default to true]
**httpLoggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if HTTP logging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**ipSecurityRestrictions** | [**[AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner]**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.md) | IP security restrictions for main. | [optional] 
**javaContainer** | **String** | Java container. | [optional] 
**javaContainerVersion** | **String** | Java container version. | [optional] 
**javaVersion** | **String** | Java version. | [optional] 
**limits** | [**AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigLimits**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigLimits.md) |  | [optional] 
**linuxFxVersion** | **String** | Linux App Framework and version | [optional] 
**loadBalancing** | **String** | Site load balancing. | [optional] 
**localMySqlEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to enable local MySQL; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] [default to false]
**logsDirectorySizeLimit** | **Number** | HTTP logs directory size limit. | [optional] 
**machineKey** | [**AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigMachineKey**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigMachineKey.md) |  | [optional] 
**managedPipelineMode** | **String** | Managed pipeline mode. | [optional] 
**managedServiceIdentityId** | **Number** | Managed Service Identity Id | [optional] 
**minTlsVersion** | **String** | MinTlsVersion: configures the minimum version of TLS required for SSL requests | [optional] 
**netFrameworkVersion** | **String** | .NET Framework version. | [optional] [default to &#39;v4.6&#39;]
**nodeVersion** | **String** | Version of Node.js. | [optional] 
**numberOfWorkers** | **Number** | Number of workers. | [optional] 
**phpVersion** | **String** | Version of PHP. | [optional] 
**preWarmedInstanceCount** | **Number** | Number of preWarmed instances. This setting only applies to the Consumption and Elastic Plans | [optional] 
**publishingUsername** | **String** | Publishing user name. | [optional] 
**push** | [**AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigPush**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigPush.md) |  | [optional] 
**pythonVersion** | **String** | Version of Python. | [optional] 
**remoteDebuggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if remote debugging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**remoteDebuggingVersion** | **String** | Remote debugging version. | [optional] 
**requestTracingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if request tracing is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**requestTracingExpirationTime** | **Date** | Request tracing expiration time. | [optional] 
**scmIpSecurityRestrictions** | [**[AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner]**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.md) | IP security restrictions for scm. | [optional] 
**scmIpSecurityRestrictionsUseMain** | **Boolean** | IP security restrictions for scm to use main. | [optional] 
**scmType** | **String** | SCM type. | [optional] 
**tracingOptions** | **String** | Tracing options. | [optional] 
**use32BitWorkerProcess** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to use 32-bit worker process; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**virtualApplications** | [**[AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInner]**](AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInner.md) | Virtual applications. | [optional] 
**vnetName** | **String** | Virtual Network name. | [optional] 
**webSocketsEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if WebSocket is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**windowsFxVersion** | **String** | Xenon App Framework and version | [optional] 
**xManagedServiceIdentityId** | **Number** | Explicit Managed Service Identity Id | [optional] 



## Enum: FtpsStateEnum


* `AllAllowed` (value: `"AllAllowed"`)

* `FtpsOnly` (value: `"FtpsOnly"`)

* `Disabled` (value: `"Disabled"`)





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

* `VSTSRM` (value: `"VSTSRM"`)




