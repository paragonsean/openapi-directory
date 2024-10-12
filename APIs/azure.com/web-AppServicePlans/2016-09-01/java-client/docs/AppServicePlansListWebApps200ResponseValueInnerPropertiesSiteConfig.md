

# AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig

Configuration of an App Service app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alwaysOn** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if Always On is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**apiDefinition** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigApiDefinition**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigApiDefinition.md) |  |  [optional] |
|**appCommandLine** | **String** | App command line to launch. |  [optional] |
|**appSettings** | [**List&lt;AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAppSettingsInner&gt;**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAppSettingsInner.md) | Application settings. |  [optional] |
|**autoHealEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if Auto Heal is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**autoHealRules** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules.md) |  |  [optional] |
|**autoSwapSlotName** | **String** | Auto-swap slot name. |  [optional] |
|**connectionStrings** | [**List&lt;AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner&gt;**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner.md) | Connection strings. |  [optional] |
|**cors** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigCors**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigCors.md) |  |  [optional] |
|**defaultDocuments** | **List&lt;String&gt;** | Default documents. |  [optional] |
|**detailedErrorLoggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if detailed error logging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**documentRoot** | **String** | Document root. |  [optional] |
|**experiments** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments.md) |  |  [optional] |
|**handlerMappings** | [**List&lt;AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigHandlerMappingsInner&gt;**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigHandlerMappingsInner.md) | Handler mappings. |  [optional] |
|**http20Enabled** | **Boolean** | Http20Enabled: configures a web site to allow clients to connect over http2.0 |  [optional] |
|**httpLoggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if HTTP logging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**ipSecurityRestrictions** | [**List&lt;AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner&gt;**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner.md) | IP security restrictions. |  [optional] |
|**javaContainer** | **String** | Java container. |  [optional] |
|**javaContainerVersion** | **String** | Java container version. |  [optional] |
|**javaVersion** | **String** | Java version. |  [optional] |
|**limits** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits.md) |  |  [optional] |
|**linuxFxVersion** | **String** | Linux App Framework and version |  [optional] |
|**loadBalancing** | [**LoadBalancingEnum**](#LoadBalancingEnum) | Site load balancing. |  [optional] |
|**localMySqlEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to enable local MySQL; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**logsDirectorySizeLimit** | **Integer** | HTTP logs directory size limit. |  [optional] |
|**machineKey** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey.md) |  |  [optional] |
|**managedPipelineMode** | [**ManagedPipelineModeEnum**](#ManagedPipelineModeEnum) | Managed pipeline mode. |  [optional] |
|**minTlsVersion** | [**MinTlsVersionEnum**](#MinTlsVersionEnum) | MinTlsVersion: configures the minimum version of TLS required for SSL requests |  [optional] |
|**netFrameworkVersion** | **String** | .NET Framework version. |  [optional] |
|**nodeVersion** | **String** | Version of Node.js. |  [optional] |
|**numberOfWorkers** | **Integer** | Number of workers. |  [optional] |
|**phpVersion** | **String** | Version of PHP. |  [optional] |
|**publishingUsername** | **String** | Publishing user name. |  [optional] |
|**push** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush.md) |  |  [optional] |
|**pythonVersion** | **String** | Version of Python. |  [optional] |
|**remoteDebuggingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if remote debugging is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**remoteDebuggingVersion** | **String** | Remote debugging version. |  [optional] |
|**requestTracingEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if request tracing is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**requestTracingExpirationTime** | **OffsetDateTime** | Request tracing expiration time. |  [optional] |
|**scmType** | [**ScmTypeEnum**](#ScmTypeEnum) | SCM type. |  [optional] |
|**tracingOptions** | **String** | Tracing options. |  [optional] |
|**use32BitWorkerProcess** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to use 32-bit worker process; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**virtualApplications** | [**List&lt;AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInner&gt;**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInner.md) | Virtual applications. |  [optional] |
|**vnetName** | **String** | Virtual Network name. |  [optional] |
|**webSocketsEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if WebSocket is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |



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



