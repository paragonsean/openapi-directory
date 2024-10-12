

# GooglePrivacyDlpV2DiscoveryConfig

Configuration for discovery to scan resources for profile generation. Only one discovery configuration may exist per organization, folder, or project. The generated data profiles are retained according to the [data retention policy] (https://cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**List&lt;GooglePrivacyDlpV2DataProfileAction&gt;**](GooglePrivacyDlpV2DataProfileAction.md) | Actions to execute at the completion of scanning. |  [optional] |
|**createTime** | **String** | Output only. The creation timestamp of a DiscoveryConfig. |  [optional] [readonly] |
|**displayName** | **String** | Display name (max 100 chars) |  [optional] |
|**errors** | [**List&lt;GooglePrivacyDlpV2Error&gt;**](GooglePrivacyDlpV2Error.md) | Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared. |  [optional] [readonly] |
|**inspectTemplates** | **List&lt;String&gt;** | Detection logic for profile generation. Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery. Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including \&quot;global\&quot;). Each region is scanned using the applicable template. If no region-specific template is specified, but a \&quot;global\&quot; template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region&#39;s data will not be scanned. For more information, see https://cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency. |  [optional] |
|**lastRunTime** | **String** | Output only. The timestamp of the last time this config was executed. |  [optional] [readonly] |
|**name** | **String** | Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example &#x60;projects/dlp-test-project/locations/global/discoveryConfigs/53234423&#x60;. |  [optional] |
|**orgConfig** | [**GooglePrivacyDlpV2OrgConfig**](GooglePrivacyDlpV2OrgConfig.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Required. A status for this configuration. |  [optional] |
|**targets** | [**List&lt;GooglePrivacyDlpV2DiscoveryTarget&gt;**](GooglePrivacyDlpV2DiscoveryTarget.md) | Target to match against for determining what to scan and how frequently. |  [optional] |
|**updateTime** | **String** | Output only. The last update timestamp of a DiscoveryConfig. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| PAUSED | &quot;PAUSED&quot; |



