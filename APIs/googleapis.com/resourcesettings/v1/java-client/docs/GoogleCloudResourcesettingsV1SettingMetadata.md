

# GoogleCloudResourcesettingsV1SettingMetadata

Metadata about a setting which is not editable by the end user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataType** | [**DataTypeEnum**](#DataTypeEnum) | The data type for this setting. |  [optional] |
|**defaultValue** | [**GoogleCloudResourcesettingsV1Value**](GoogleCloudResourcesettingsV1Value.md) |  |  [optional] |
|**description** | **String** | A detailed description of what this setting does. |  [optional] |
|**displayName** | **String** | The human readable name for this setting. |  [optional] |
|**readOnly** | **Boolean** | A flag indicating that values of this setting cannot be modified. See documentation for the specific setting for updates and reasons. |  [optional] |



## Enum: DataTypeEnum

| Name | Value |
|---- | -----|
| DATA_TYPE_UNSPECIFIED | &quot;DATA_TYPE_UNSPECIFIED&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |
| STRING | &quot;STRING&quot; |
| STRING_SET | &quot;STRING_SET&quot; |
| ENUM_VALUE | &quot;ENUM_VALUE&quot; |
| DURATION_VALUE | &quot;DURATION_VALUE&quot; |
| STRING_MAP | &quot;STRING_MAP&quot; |



