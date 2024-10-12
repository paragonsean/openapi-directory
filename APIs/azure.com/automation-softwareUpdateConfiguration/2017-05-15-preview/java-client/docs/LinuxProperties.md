

# LinuxProperties

Linux specific update configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**excludedPackageNameMasks** | **List&lt;String&gt;** | packages excluded from the software update configuration. |  [optional] |
|**includedPackageClassifications** | [**IncludedPackageClassificationsEnum**](#IncludedPackageClassificationsEnum) | Update classifications included in the software update configuration. |  [optional] |
|**includedPackageNameMasks** | **List&lt;String&gt;** | packages included from the software update configuration. |  [optional] |
|**rebootSetting** | **String** | Reboot setting for the software update configuration. |  [optional] |



## Enum: IncludedPackageClassificationsEnum

| Name | Value |
|---- | -----|
| UNCLASSIFIED | &quot;Unclassified&quot; |
| CRITICAL | &quot;Critical&quot; |
| SECURITY | &quot;Security&quot; |
| OTHER | &quot;Other&quot; |



