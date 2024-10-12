

# WindowsProperties

Windows specific update configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**excludedKbNumbers** | **List&lt;String&gt;** | KB numbers excluded from the software update configuration. |  [optional] |
|**includedKbNumbers** | **List&lt;String&gt;** | KB numbers included from the software update configuration. |  [optional] |
|**includedUpdateClassifications** | [**IncludedUpdateClassificationsEnum**](#IncludedUpdateClassificationsEnum) | Update classification included in the software update configuration. A comma separated string with required values |  [optional] |
|**rebootSetting** | **String** | Reboot setting for the software update configuration. |  [optional] |



## Enum: IncludedUpdateClassificationsEnum

| Name | Value |
|---- | -----|
| UNCLASSIFIED | &quot;Unclassified&quot; |
| CRITICAL | &quot;Critical&quot; |
| SECURITY | &quot;Security&quot; |
| UPDATE_ROLLUP | &quot;UpdateRollup&quot; |
| FEATURE_PACK | &quot;FeaturePack&quot; |
| SERVICE_PACK | &quot;ServicePack&quot; |
| DEFINITION | &quot;Definition&quot; |
| TOOLS | &quot;Tools&quot; |
| UPDATES | &quot;Updates&quot; |



