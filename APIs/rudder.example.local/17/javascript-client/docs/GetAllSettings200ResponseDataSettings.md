# RudderApi.GetAllSettings200ResponseDataSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedNetworks** | [**[GetAllSettings200ResponseDataSettingsAllowedNetworksInner]**](GetAllSettings200ResponseDataSettingsAllowedNetworksInner.md) | List of allowed networks for each policy server (root and relays) | [optional] 
**changeMessagePrompt** | **String** | Explanation to display | [optional] 
**displayRecentChangesGraphs** | **Boolean** | Display changes graphs | [optional] 
**enableChangeMessage** | **Boolean** | Enable change audit logs | [optional] 
**enableChangeRequest** | **Boolean** | Enable Change Requests | [optional] 
**enableJavascriptDirectives** | **String** | Enable script evaluation in Directives | [optional] 
**enableSelfDeployment** | **Boolean** | Allow self deployment | [optional] 
**enableSelfValidation** | **Boolean** | Allow self validation | [optional] 
**firstRunHour** | **Number** | First agent run time - hour | [optional] 
**firstRunMinute** | **Number** | First agent run time - minute | [optional] 
**globalPolicyMode** | **String** | Define the default setting for global policy mode | [optional] 
**globalPolicyModeOverridable** | **Boolean** | Allow overrides on this default setting | [optional] 
**heartbeatFrequency** | **Number** | Send heartbeat every heartbeat_frequency runs (only on **changes-only** compliance mode) | [optional] 
**mandatoryChangeMessage** | **Boolean** | Make message mandatory | [optional] 
**modifiedFileTtl** | **Number** | Number of days to retain modified files | [optional] 
**nodeAcceptDuplicatedHostname** | **Boolean** | Allow acceptation of a pending node when another one with the same hostname is already accepted | [optional] [default to false]
**nodeOnacceptDefaultPolicyMode** | **String** | Default policy mode for accepted node | [optional] 
**nodeOnacceptDefaultState** | **String** | Set default state for node when they are accepted within Rudder | [optional] 
**outputFileTtl** | **Number** | Number of days to retain agent output files | [optional] 
**relayServerSynchronizationMethod** | **String** | Method used to synchronize data between server and relays, either \&quot;classic\&quot; (agent protocol, default), \&quot;rsync\&quot; (use rsync to synchronize, that you&#39;ll need to be manually set up), or \&quot;disabled\&quot; (use third party system to transmit data) | [optional] 
**relayServerSynchronizePolicies** | **Boolean** | If **rsync** is set as a synchronization method, use rsync to synchronize policies between Rudder server and relays. If false, you&#39;ll have to synchronize policies yourself. | [optional] 
**relayServerSynchronizeSharedFiles** | **Boolean** | If **rsync** is set as a synchronization method, use rsync to synchronize shared files between Rudder server and relays. If false, you&#39;ll have to synchronize shared files yourself. | [optional] 
**reportingMode** | **String** | Compliance reporting mode | [optional] 
**requireTimeSynchronization** | **Boolean** | Require time synchronization between nodes and policy server | [optional] 
**rudderComputeChanges** | **Boolean** | Compute list of changes (repaired reports) per rule | [optional] [default to true]
**rudderComputeDyngroupsMaxParallelism** | **String** | Set the parallelism to compute dynamic group, as a number of thread (i.e. 4), or a multiplicative of the number of core (x0.5) | [optional] [default to &#39;1&#39;]
**rudderGenerationComputeDyngroups** | **Boolean** | Recompute all dynamic groups at the start of policy generation | [optional] [default to true]
**rudderGenerationContinueOnError** | **Boolean** | Policy generation continues on error during NodeConfiguration evaluation | [optional] [default to false]
**rudderGenerationDelay** | **String** | Set a delay before starting policy generation, this will allow you to accumulate changes before they are deployed to Nodes, and can also lessen webapp resources needs. The value is a number followed by the time unit needed (seconds/s, minutes/m, hours/h ...), ie \&quot;5m\&quot; for 5 minutes | [optional] [default to &#39;0 seconds&#39;]
**rudderGenerationJsTimeout** | **Number** | Policy generation JS evaluation of directive parameter timeout in seconds | [optional] [default to 30]
**rudderGenerationMaxParallelism** | **String** | Set the policy generation parallelism, either as an number of thread (i.e. 4), or a multiplicative of the number of core (x0.5) | [optional] [default to &#39;x0.5&#39;]
**rudderGenerationPolicy** | **String** | Should policy generation be triggered automatically after a change (value &#39;all&#39;), or should we wait until a manual launch (through api or UI, value &#39;onlyManual&#39;) or even no policy generation at all (value \&quot;none\&quot;) | [optional] [default to &#39;all&#39;]
**rudderReportProtocolDefault** | **String** | Default reporting protocol used | [optional] 
**rudderSaveDbComplianceDetails** | **Boolean** | Store all compliance details in database | [optional] [default to false]
**rudderSaveDbComplianceLevels** | **Boolean** | Store all compliance levels in database | [optional] [default to true]
**rudderVerifyCertificates** | **Boolean** | Enforce certificate validation in all HTTPS calls | [optional] [default to false]
**runFrequency** | **Number** | Agent run schedule - time between agent runs (in minutes) | [optional] 
**sendMetrics** | **String** | Send anonymous usage statistics | [optional] 
**splayTime** | **Number** | Maximum delay after scheduled run time (random interval) | [optional] 
**unexpectedUnboundVarValues** | **Boolean** | Allows multiple reports for configuration based on a multivalued variable | [optional] [default to true]



## Enum: GlobalPolicyModeEnum


* `enforce` (value: `"enforce"`)

* `audit` (value: `"audit"`)





## Enum: NodeOnacceptDefaultPolicyModeEnum


* `default` (value: `"default"`)

* `enforce` (value: `"enforce"`)

* `audit` (value: `"audit"`)





## Enum: NodeOnacceptDefaultStateEnum


* `enabled` (value: `"enabled"`)

* `ignored` (value: `"ignored"`)

* `empty-policies` (value: `"empty-policies"`)

* `initializing` (value: `"initializing"`)

* `preparing-eol` (value: `"preparing-eol"`)





## Enum: RelayServerSynchronizationMethodEnum


* `classic` (value: `"classic"`)

* `rsync` (value: `"rsync"`)

* `disabled` (value: `"disabled"`)





## Enum: ReportingModeEnum


* `full-compliance` (value: `"full-compliance"`)

* `changes-only` (value: `"changes-only"`)

* `reports-disabled` (value: `"reports-disabled"`)





## Enum: RudderReportProtocolDefaultEnum


* `HTTPS` (value: `"HTTPS"`)

* `SYSLOG` (value: `"SYSLOG"`)




