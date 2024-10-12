

# EnvironmentSettingPropertiesFragment

Properties of an environment setting

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationState** | [**ConfigurationStateEnum**](#ConfigurationStateEnum) | Describes the user&#39;s progress in configuring their environment setting |  [optional] |
|**description** | **String** | Describes the environment and its resource settings |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**resourceSettings** | [**ResourceSettingsFragment**](ResourceSettingsFragment.md) |  |  [optional] |
|**title** | **String** | Brief title describing the environment and its resource settings |  [optional] |
|**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). |  [optional] |



## Enum: ConfigurationStateEnum

| Name | Value |
|---- | -----|
| NOT_APPLICABLE | &quot;NotApplicable&quot; |
| COMPLETED | &quot;Completed&quot; |



