

# LabAnnouncementPropertiesFragment

Properties of a lab's announcement banner

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | [**EnabledEnum**](#EnabledEnum) | Is the lab announcement active/enabled at this time? |  [optional] |
|**expirationDate** | **OffsetDateTime** | The time at which the announcement expires (null for never) |  [optional] |
|**expired** | **Boolean** | Has this announcement expired? |  [optional] |
|**markdown** | **String** | The markdown text (if any) that this lab displays in the UI. If left empty/null, nothing will be shown. |  [optional] |
|**title** | **String** | The plain text title for the lab announcement |  [optional] |



## Enum: EnabledEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



