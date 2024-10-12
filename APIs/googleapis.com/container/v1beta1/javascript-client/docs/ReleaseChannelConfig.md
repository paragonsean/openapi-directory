# KubernetesEngineApi.ReleaseChannelConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableVersions** | [**[AvailableVersion]**](AvailableVersion.md) | Deprecated. This field has been deprecated and replaced with the valid_versions field. | [optional] 
**channel** | **String** | The release channel this configuration applies to. | [optional] 
**defaultVersion** | **String** | The default version for newly created clusters on the channel. | [optional] 
**validVersions** | **[String]** | List of valid versions for the channel. | [optional] 



## Enum: ChannelEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `RAPID` (value: `"RAPID"`)

* `REGULAR` (value: `"REGULAR"`)

* `STABLE` (value: `"STABLE"`)




