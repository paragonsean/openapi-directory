

# GetAllSettings200ResponseDataSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedNetworks** | [**List&lt;GetAllSettings200ResponseDataSettingsAllowedNetworksInner&gt;**](GetAllSettings200ResponseDataSettingsAllowedNetworksInner.md) | List of allowed networks for each policy server (root and relays) |  [optional] |
|**changeMessagePrompt** | **String** | Explanation to display |  [optional] |
|**displayRecentChangesGraphs** | **Boolean** | Display changes graphs |  [optional] |
|**enableChangeMessage** | **Boolean** | Enable change audit logs |  [optional] |
|**enableChangeRequest** | **Boolean** | Enable Change Requests |  [optional] |
|**enableJavascriptDirectives** | **String** | Enable script evaluation in Directives |  [optional] |
|**enableSelfDeployment** | **Boolean** | Allow self deployment |  [optional] |
|**enableSelfValidation** | **Boolean** | Allow self validation |  [optional] |
|**firstRunHour** | **Integer** | First agent run time - hour |  [optional] |
|**firstRunMinute** | **Integer** | First agent run time - minute |  [optional] |
|**globalPolicyMode** | [**GlobalPolicyModeEnum**](#GlobalPolicyModeEnum) | Define the default setting for global policy mode |  [optional] |
|**globalPolicyModeOverridable** | **Boolean** | Allow overrides on this default setting |  [optional] |
|**heartbeatFrequency** | **Integer** | Send heartbeat every heartbeat_frequency runs (only on **changes-only** compliance mode) |  [optional] |
|**mandatoryChangeMessage** | **Boolean** | Make message mandatory |  [optional] |
|**modifiedFileTtl** | **Integer** | Number of days to retain modified files |  [optional] |
|**nodeAcceptDuplicatedHostname** | **Boolean** | Allow acceptation of a pending node when another one with the same hostname is already accepted |  [optional] |
|**nodeOnacceptDefaultPolicyMode** | [**NodeOnacceptDefaultPolicyModeEnum**](#NodeOnacceptDefaultPolicyModeEnum) | Default policy mode for accepted node |  [optional] |
|**nodeOnacceptDefaultState** | [**NodeOnacceptDefaultStateEnum**](#NodeOnacceptDefaultStateEnum) | Set default state for node when they are accepted within Rudder |  [optional] |
|**outputFileTtl** | **Integer** | Number of days to retain agent output files |  [optional] |
|**relayServerSynchronizationMethod** | [**RelayServerSynchronizationMethodEnum**](#RelayServerSynchronizationMethodEnum) | Method used to synchronize data between server and relays, either \&quot;classic\&quot; (agent protocol, default), \&quot;rsync\&quot; (use rsync to synchronize, that you&#39;ll need to be manually set up), or \&quot;disabled\&quot; (use third party system to transmit data) |  [optional] |
|**relayServerSynchronizePolicies** | **Boolean** | If **rsync** is set as a synchronization method, use rsync to synchronize policies between Rudder server and relays. If false, you&#39;ll have to synchronize policies yourself. |  [optional] |
|**relayServerSynchronizeSharedFiles** | **Boolean** | If **rsync** is set as a synchronization method, use rsync to synchronize shared files between Rudder server and relays. If false, you&#39;ll have to synchronize shared files yourself. |  [optional] |
|**reportingMode** | [**ReportingModeEnum**](#ReportingModeEnum) | Compliance reporting mode |  [optional] |
|**requireTimeSynchronization** | **Boolean** | Require time synchronization between nodes and policy server |  [optional] |
|**rudderComputeChanges** | **Boolean** | Compute list of changes (repaired reports) per rule |  [optional] |
|**rudderComputeDyngroupsMaxParallelism** | **String** | Set the parallelism to compute dynamic group, as a number of thread (i.e. 4), or a multiplicative of the number of core (x0.5) |  [optional] |
|**rudderGenerationComputeDyngroups** | **Boolean** | Recompute all dynamic groups at the start of policy generation |  [optional] |
|**rudderGenerationContinueOnError** | **Boolean** | Policy generation continues on error during NodeConfiguration evaluation |  [optional] |
|**rudderGenerationDelay** | **String** | Set a delay before starting policy generation, this will allow you to accumulate changes before they are deployed to Nodes, and can also lessen webapp resources needs. The value is a number followed by the time unit needed (seconds/s, minutes/m, hours/h ...), ie \&quot;5m\&quot; for 5 minutes |  [optional] |
|**rudderGenerationJsTimeout** | **Integer** | Policy generation JS evaluation of directive parameter timeout in seconds |  [optional] |
|**rudderGenerationMaxParallelism** | **String** | Set the policy generation parallelism, either as an number of thread (i.e. 4), or a multiplicative of the number of core (x0.5) |  [optional] |
|**rudderGenerationPolicy** | **String** | Should policy generation be triggered automatically after a change (value &#39;all&#39;), or should we wait until a manual launch (through api or UI, value &#39;onlyManual&#39;) or even no policy generation at all (value \&quot;none\&quot;) |  [optional] |
|**rudderReportProtocolDefault** | [**RudderReportProtocolDefaultEnum**](#RudderReportProtocolDefaultEnum) | Default reporting protocol used |  [optional] |
|**rudderSaveDbComplianceDetails** | **Boolean** | Store all compliance details in database |  [optional] |
|**rudderSaveDbComplianceLevels** | **Boolean** | Store all compliance levels in database |  [optional] |
|**rudderVerifyCertificates** | **Boolean** | Enforce certificate validation in all HTTPS calls |  [optional] |
|**runFrequency** | **Integer** | Agent run schedule - time between agent runs (in minutes) |  [optional] |
|**sendMetrics** | **String** | Send anonymous usage statistics |  [optional] |
|**splayTime** | **Integer** | Maximum delay after scheduled run time (random interval) |  [optional] |
|**unexpectedUnboundVarValues** | **Boolean** | Allows multiple reports for configuration based on a multivalued variable |  [optional] |



## Enum: GlobalPolicyModeEnum

| Name | Value |
|---- | -----|
| ENFORCE | &quot;enforce&quot; |
| AUDIT | &quot;audit&quot; |



## Enum: NodeOnacceptDefaultPolicyModeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| ENFORCE | &quot;enforce&quot; |
| AUDIT | &quot;audit&quot; |



## Enum: NodeOnacceptDefaultStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| IGNORED | &quot;ignored&quot; |
| EMPTY_POLICIES | &quot;empty-policies&quot; |
| INITIALIZING | &quot;initializing&quot; |
| PREPARING_EOL | &quot;preparing-eol&quot; |



## Enum: RelayServerSynchronizationMethodEnum

| Name | Value |
|---- | -----|
| CLASSIC | &quot;classic&quot; |
| RSYNC | &quot;rsync&quot; |
| DISABLED | &quot;disabled&quot; |



## Enum: ReportingModeEnum

| Name | Value |
|---- | -----|
| FULL_COMPLIANCE | &quot;full-compliance&quot; |
| CHANGES_ONLY | &quot;changes-only&quot; |
| REPORTS_DISABLED | &quot;reports-disabled&quot; |



## Enum: RudderReportProtocolDefaultEnum

| Name | Value |
|---- | -----|
| HTTPS | &quot;HTTPS&quot; |
| SYSLOG | &quot;SYSLOG&quot; |



