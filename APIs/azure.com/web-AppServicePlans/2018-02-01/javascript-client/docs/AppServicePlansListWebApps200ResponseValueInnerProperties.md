# AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityState** | **String** | Management information availability state for the app. | [optional] [readonly] 
**clientAffinityEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to enable client affinity; &lt;code&gt;false&lt;/code&gt; to stop sending session affinity cookies, which route client requests in the same session to the same instance. Default is &lt;code&gt;true&lt;/code&gt;. | [optional] 
**clientCertEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to enable client certificate authentication (TLS mutual authentication); otherwise, &lt;code&gt;false&lt;/code&gt;. Default is &lt;code&gt;false&lt;/code&gt;. | [optional] 
**clientCertExclusionPaths** | **String** | client certificate authentication comma-separated exclusion paths | [optional] 
**cloningInfo** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo**](AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.md) |  | [optional] 
**containerSize** | **Number** | Size of the function container. | [optional] 
**dailyMemoryTimeQuota** | **Number** | Maximum allowed daily memory-time quota (applicable on dynamic apps only). | [optional] 
**defaultHostName** | **String** | Default hostname of the app. Read-only. | [optional] [readonly] 
**enabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if the app is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. Setting this value to false disables the app (takes the app offline). | [optional] 
**enabledHostNames** | **[String]** | Enabled hostnames for the app.Hostnames need to be assigned (see HostNames) AND enabled. Otherwise, the app is not served on those hostnames. | [optional] [readonly] 
**geoDistributions** | [**[AppServicePlansListWebApps200ResponseValueInnerPropertiesGeoDistributionsInner]**](AppServicePlansListWebApps200ResponseValueInnerPropertiesGeoDistributionsInner.md) | GeoDistributions for this site | [optional] 
**hostNameSslStates** | [**[AppServicePlansListWebApps200ResponseValueInnerPropertiesHostNameSslStatesInner]**](AppServicePlansListWebApps200ResponseValueInnerPropertiesHostNameSslStatesInner.md) | Hostname SSL states are used to manage the SSL bindings for app&#39;s hostnames. | [optional] 
**hostNames** | **[String]** | Hostnames associated with the app. | [optional] [readonly] 
**hostNamesDisabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to disable the public hostnames of the app; otherwise, &lt;code&gt;false&lt;/code&gt;.  If &lt;code&gt;true&lt;/code&gt;, the app is only accessible via API management process. | [optional] 
**hostingEnvironmentProfile** | [**AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile**](AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile.md) |  | [optional] 
**httpsOnly** | **Boolean** | HttpsOnly: configures a web site to accept only https requests. Issues redirect for http requests | [optional] 
**hyperV** | **Boolean** | Hyper-V sandbox. | [optional] [default to false]
**inProgressOperationId** | **String** | Specifies an operation id if this site has a pending operation. | [optional] [readonly] 
**isDefaultContainer** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if the app is a default container; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] [readonly] 
**isXenon** | **Boolean** | Obsolete: Hyper-V sandbox. | [optional] [default to false]
**lastModifiedTimeUtc** | **Date** | Last time the app was modified, in UTC. Read-only. | [optional] [readonly] 
**maxNumberOfWorkers** | **Number** | Maximum number of workers. This only applies to Functions container. | [optional] [readonly] 
**outboundIpAddresses** | **String** | List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from tenants that site can be hosted with current settings. Read-only. | [optional] [readonly] 
**possibleOutboundIpAddresses** | **String** | List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from all tenants. Read-only. | [optional] [readonly] 
**redundancyMode** | **String** | Site redundancy mode | [optional] 
**repositorySiteName** | **String** | Name of the repository site. | [optional] [readonly] 
**reserved** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if reserved; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] [default to false]
**resourceGroup** | **String** | Name of the resource group the app belongs to. Read-only. | [optional] [readonly] 
**scmSiteAlsoStopped** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to stop SCM (KUDU) site when the app is stopped; otherwise, &lt;code&gt;false&lt;/code&gt;. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] [default to false]
**serverFarmId** | **String** | Resource ID of the associated App Service plan, formatted as: \&quot;/subscriptions/{subscriptionID}/resourceGroups/{groupName}/providers/Microsoft.Web/serverfarms/{appServicePlanName}\&quot;. | [optional] 
**siteConfig** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig.md) |  | [optional] 
**slotSwapStatus** | [**AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus**](AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus.md) |  | [optional] 
**state** | **String** | Current state of the app. | [optional] [readonly] 
**suspendedTill** | **Date** | App suspended till in case memory-time quota is exceeded. | [optional] [readonly] 
**targetSwapSlot** | **String** | Specifies which deployment slot this app will swap into. Read-only. | [optional] [readonly] 
**trafficManagerHostNames** | **[String]** | Azure Traffic Manager hostnames associated with the app. Read-only. | [optional] [readonly] 
**usageState** | **String** | State indicating whether the app has exceeded its quota usage. Read-only. | [optional] [readonly] 



## Enum: AvailabilityStateEnum


* `Normal` (value: `"Normal"`)

* `Limited` (value: `"Limited"`)

* `DisasterRecoveryMode` (value: `"DisasterRecoveryMode"`)





## Enum: RedundancyModeEnum


* `None` (value: `"None"`)

* `Manual` (value: `"Manual"`)

* `Failover` (value: `"Failover"`)

* `ActiveActive` (value: `"ActiveActive"`)

* `GeoRedundant` (value: `"GeoRedundant"`)





## Enum: UsageStateEnum


* `Normal` (value: `"Normal"`)

* `Exceeded` (value: `"Exceeded"`)




