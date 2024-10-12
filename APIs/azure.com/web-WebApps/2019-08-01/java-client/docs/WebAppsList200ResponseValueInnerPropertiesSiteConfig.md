

# WebAppsList200ResponseValueInnerPropertiesSiteConfig

Configuration of an App Service app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alwaysOn** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if Always On is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**apiDefinition** | [**WebAppsList200ResponseValueInnerPropertiesSiteConfigApiDefinition**](WebAppsList200ResponseValueInnerPropertiesSiteConfigApiDefinition.md) |  |  [optional] |
|**apiManagementConfig** | [**WebAppsList200ResponseValueInnerPropertiesSiteConfigApiManagementConfig**](WebAppsList200ResponseValueInnerPropertiesSiteConfigApiManagementConfig.md) |  |  [optional] |
|**appCommandLine** | **String** | App command line to launch. |  [optional] |
|**appSettings** | [**List&lt;WebAppsList200ResponseValueInnerPropertiesSiteConfigAppSettingsInner&gt;**](WebAppsList200ResponseValueInnerPropertiesSiteConfigAppSettingsInner.md) | Application settings. |  [optional] |
|**autoHealEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if Auto Heal is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**autoHealRules** | [**WebAppsList200ResponseValueInnerPropertiesSiteConfigAutoHealRules**](WebAppsList200ResponseValueInnerPropertiesSiteConfigAutoHealRules.md) |  |  [optional] |
|**autoSwapSlotName** | **String** | Auto-swap slot name. |  [optional] |
|**connectionStrings** | [**List&lt;WebAppsList200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner&gt;**](WebAppsList200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner.md) | Connection strings. |  [optional] |
|**cors** | [**WebAppsList200ResponseValueInnerPropertiesSiteConfigCors**](WebAppsList200ResponseValueInnerPropertiesSiteConfigCors.md) |  |  [optional] |
|**defaultDocuments** | **List&lt;String&gt;** | Default documents. |  [optional] |
|**detailedErrorLoggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if detailed error logging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**documentRoot** | **String** | Document root. |  [optional] |
|**experiments** | [**WebAppsList200ResponseValueInnerPropertiesSiteConfigExperiments**](WebAppsList200ResponseValueInnerPropertiesSiteConfigExperiments.md) |  |  [optional] |
|**ftpsState** | [**FtpsStateEnum**](#FtpsStateEnum) | State of FTP / FTPS service |  [optional] |
|**handlerMappings** | [**List&lt;WebAppsList200ResponseValueInnerPropertiesSiteConfigHandlerMappingsInner&gt;**](WebAppsList200ResponseValueInnerPropertiesSiteConfigHandlerMappingsInner.md) | Handler mappings. |  [optional] |
|**healthCheckPath** | **String** | Health check path |  [optional] |
|**http20Enabled** | **Boolean** | Http20Enabled: configures a web site to allow clients to connect over http2.0 |  [optional] |
|**httpLoggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if HTTP logging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**ipSecurityRestrictions** | [**List&lt;WebAppsList200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner&gt;**](WebAppsList200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.md) | IP security restrictions for main. |  [optional] |
|**javaContainer** | **String** | Java container. |  [optional] |
|**javaContainerVersion** | **String** | Java container version. |  [optional] |
|**javaVersion** | **String** | Java version. |  [optional] |
|**limits** | [**WebAppsList200ResponseValueInnerPropertiesSiteConfigLimits**](WebAppsList200ResponseValueInnerPropertiesSiteConfigLimits.md) |  |  [optional] |
|**linuxFxVersion** | **String** | Linux App Framework and version |  [optional] |
|**loadBalancing** | [**LoadBalancingEnum**](#LoadBalancingEnum) | Site load balancing. |  [optional] |
|**localMySqlEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to enable local MySQL; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**logsDirectorySizeLimit** | **Integer** | HTTP logs directory size limit. |  [optional] |
|**machineKey** | [**WebAppsList200ResponseValueInnerPropertiesSiteConfigMachineKey**](WebAppsList200ResponseValueInnerPropertiesSiteConfigMachineKey.md) |  |  [optional] |
|**managedPipelineMode** | [**ManagedPipelineModeEnum**](#ManagedPipelineModeEnum) | Managed pipeline mode. |  [optional] |
|**managedServiceIdentityId** | **Integer** | Managed Service Identity Id |  [optional] |
|**minTlsVersion** | [**MinTlsVersionEnum**](#MinTlsVersionEnum) | MinTlsVersion: configures the minimum version of TLS required for SSL requests |  [optional] |
|**netFrameworkVersion** | **String** | .NET Framework version. |  [optional] |
|**nodeVersion** | **String** | Version of Node.js. |  [optional] |
|**numberOfWorkers** | **Integer** | Number of workers. |  [optional] |
|**phpVersion** | **String** | Version of PHP. |  [optional] |
|**preWarmedInstanceCount** | **Integer** | Number of preWarmed instances. This setting only applies to the Consumption and Elastic Plans |  [optional] |
|**publishingUsername** | **String** | Publishing user name. |  [optional] |
|**push** | [**WebAppsList200ResponseValueInnerPropertiesSiteConfigPush**](WebAppsList200ResponseValueInnerPropertiesSiteConfigPush.md) |  |  [optional] |
|**pythonVersion** | **String** | Version of Python. |  [optional] |
|**remoteDebuggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if remote debugging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**remoteDebuggingVersion** | **String** | Remote debugging version. |  [optional] |
|**requestTracingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if request tracing is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**requestTracingExpirationTime** | **OffsetDateTime** | Request tracing expiration time. |  [optional] |
|**scmIpSecurityRestrictions** | [**List&lt;WebAppsList200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner&gt;**](WebAppsList200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.md) | IP security restrictions for scm. |  [optional] |
|**scmIpSecurityRestrictionsUseMain** | **Boolean** | IP security restrictions for scm to use main. |  [optional] |
|**scmType** | [**ScmTypeEnum**](#ScmTypeEnum) | SCM type. |  [optional] |
|**tracingOptions** | **String** | Tracing options. |  [optional] |
|**use32BitWorkerProcess** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to use 32-bit worker process; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**virtualApplications** | [**List&lt;WebAppsList200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInner&gt;**](WebAppsList200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInner.md) | Virtual applications. |  [optional] |
|**vnetName** | **String** | Virtual Network name. |  [optional] |
|**webSocketsEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if WebSocket is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**windowsFxVersion** | **String** | Xenon App Framework and version |  [optional] |
|**xManagedServiceIdentityId** | **Integer** | Explicit Managed Service Identity Id |  [optional] |



## Enum: FtpsStateEnum

| Name | Value |
|---- | -----|
| ALL_ALLOWED | &quot;AllAllowed&quot; |
| FTPS_ONLY | &quot;FtpsOnly&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: LoadBalancingEnum

| Name | Value |
|---- | -----|
| WEIGHTED_ROUND_ROBIN | &quot;WeightedRoundRobin&quot; |
| LEAST_REQUESTS | &quot;LeastRequests&quot; |
| LEAST_RESPONSE_TIME | &quot;LeastResponseTime&quot; |
| WEIGHTED_TOTAL_TRAFFIC | &quot;WeightedTotalTraffic&quot; |
| REQUEST_HASH | &quot;RequestHash&quot; |



## Enum: ManagedPipelineModeEnum

| Name | Value |
|---- | -----|
| INTEGRATED | &quot;Integrated&quot; |
| CLASSIC | &quot;Classic&quot; |



## Enum: MinTlsVersionEnum

| Name | Value |
|---- | -----|
| _0 | &quot;1.0&quot; |
| _1 | &quot;1.1&quot; |
| _2 | &quot;1.2&quot; |



## Enum: ScmTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| DROPBOX | &quot;Dropbox&quot; |
| TFS | &quot;Tfs&quot; |
| LOCAL_GIT | &quot;LocalGit&quot; |
| GIT_HUB | &quot;GitHub&quot; |
| CODE_PLEX_GIT | &quot;CodePlexGit&quot; |
| CODE_PLEX_HG | &quot;CodePlexHg&quot; |
| BITBUCKET_GIT | &quot;BitbucketGit&quot; |
| BITBUCKET_HG | &quot;BitbucketHg&quot; |
| EXTERNAL_GIT | &quot;ExternalGit&quot; |
| EXTERNAL_HG | &quot;ExternalHg&quot; |
| ONE_DRIVE | &quot;OneDrive&quot; |
| VSO | &quot;VSO&quot; |
| VSTSRM | &quot;VSTSRM&quot; |



