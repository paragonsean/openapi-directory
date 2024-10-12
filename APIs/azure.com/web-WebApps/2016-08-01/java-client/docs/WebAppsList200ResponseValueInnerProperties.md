

# WebAppsList200ResponseValueInnerProperties

Site resource specific properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityState** | [**AvailabilityStateEnum**](#AvailabilityStateEnum) | Management information availability state for the app. |  [optional] [readonly] |
|**clientAffinityEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to enable client affinity; &lt;code&gt;false&lt;/code&gt; to stop sending session affinity cookies, which route client requests in the same session to the same instance. Default is &lt;code&gt;true&lt;/code&gt;. |  [optional] |
|**clientCertEnabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to enable client certificate authentication (TLS mutual authentication); otherwise, &lt;code&gt;false&lt;/code&gt;. Default is &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**cloningInfo** | [**WebAppsList200ResponseValueInnerPropertiesCloningInfo**](WebAppsList200ResponseValueInnerPropertiesCloningInfo.md) |  |  [optional] |
|**containerSize** | **Integer** | Size of the function container. |  [optional] |
|**dailyMemoryTimeQuota** | **Integer** | Maximum allowed daily memory-time quota (applicable on dynamic apps only). |  [optional] |
|**defaultHostName** | **String** | Default hostname of the app. Read-only. |  [optional] [readonly] |
|**enabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if the app is enabled; otherwise, &lt;code&gt;false&lt;/code&gt;. Setting this value to false disables the app (takes the app offline). |  [optional] |
|**enabledHostNames** | **List&lt;String&gt;** | Enabled hostnames for the app.Hostnames need to be assigned (see HostNames) AND enabled. Otherwise, the app is not served on those hostnames. |  [optional] [readonly] |
|**hostNameSslStates** | [**List&lt;WebAppsList200ResponseValueInnerPropertiesHostNameSslStatesInner&gt;**](WebAppsList200ResponseValueInnerPropertiesHostNameSslStatesInner.md) | Hostname SSL states are used to manage the SSL bindings for app&#39;s hostnames. |  [optional] |
|**hostNames** | **List&lt;String&gt;** | Hostnames associated with the app. |  [optional] [readonly] |
|**hostNamesDisabled** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to disable the public hostnames of the app; otherwise, &lt;code&gt;false&lt;/code&gt;.  If &lt;code&gt;true&lt;/code&gt;, the app is only accessible via API management process. |  [optional] |
|**hostingEnvironmentProfile** | [**WebAppsList200ResponseValueInnerPropertiesHostingEnvironmentProfile**](WebAppsList200ResponseValueInnerPropertiesHostingEnvironmentProfile.md) |  |  [optional] |
|**httpsOnly** | **Boolean** | HttpsOnly: configures a web site to accept only https requests. Issues redirect for http requests |  [optional] |
|**isDefaultContainer** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if the app is a default container; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] [readonly] |
|**lastModifiedTimeUtc** | **OffsetDateTime** | Last time the app was modified, in UTC. Read-only. |  [optional] [readonly] |
|**maxNumberOfWorkers** | **Integer** | Maximum number of workers. This only applies to Functions container. |  [optional] [readonly] |
|**outboundIpAddresses** | **String** | List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from tenants that site can be hosted with current settings. Read-only. |  [optional] [readonly] |
|**possibleOutboundIpAddresses** | **String** | List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from all tenants. Read-only. |  [optional] [readonly] |
|**repositorySiteName** | **String** | Name of the repository site. |  [optional] [readonly] |
|**reserved** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if reserved; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**resourceGroup** | **String** | Name of the resource group the app belongs to. Read-only. |  [optional] [readonly] |
|**scmSiteAlsoStopped** | **Boolean** | &lt;code&gt;true&lt;/code&gt; to stop SCM (KUDU) site when the app is stopped; otherwise, &lt;code&gt;false&lt;/code&gt;. The default is &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**serverFarmId** | **String** | Resource ID of the associated App Service plan, formatted as: \&quot;/subscriptions/{subscriptionID}/resourceGroups/{groupName}/providers/Microsoft.Web/serverfarms/{appServicePlanName}\&quot;. |  [optional] |
|**siteConfig** | [**WebAppsList200ResponseValueInnerPropertiesSiteConfig**](WebAppsList200ResponseValueInnerPropertiesSiteConfig.md) |  |  [optional] |
|**slotSwapStatus** | [**WebAppsList200ResponseValueInnerPropertiesSlotSwapStatus**](WebAppsList200ResponseValueInnerPropertiesSlotSwapStatus.md) |  |  [optional] |
|**snapshotInfo** | [**WebAppsList200ResponseValueInnerPropertiesSnapshotInfo**](WebAppsList200ResponseValueInnerPropertiesSnapshotInfo.md) |  |  [optional] |
|**state** | **String** | Current state of the app. |  [optional] [readonly] |
|**suspendedTill** | **OffsetDateTime** | App suspended till in case memory-time quota is exceeded. |  [optional] [readonly] |
|**targetSwapSlot** | **String** | Specifies which deployment slot this app will swap into. Read-only. |  [optional] [readonly] |
|**trafficManagerHostNames** | **List&lt;String&gt;** | Azure Traffic Manager hostnames associated with the app. Read-only. |  [optional] [readonly] |
|**usageState** | [**UsageStateEnum**](#UsageStateEnum) | State indicating whether the app has exceeded its quota usage. Read-only. |  [optional] [readonly] |



## Enum: AvailabilityStateEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;Normal&quot; |
| LIMITED | &quot;Limited&quot; |
| DISASTER_RECOVERY_MODE | &quot;DisasterRecoveryMode&quot; |



## Enum: UsageStateEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;Normal&quot; |
| EXCEEDED | &quot;Exceeded&quot; |



