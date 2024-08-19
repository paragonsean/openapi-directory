

# EncryptionSettingsProperties

The properties of EncryptionSettings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionStatus** | [**EncryptionStatusEnum**](#EncryptionStatusEnum) | The encryption status which indicates if encryption is enabled or not. |  |
|**keyRolloverStatus** | [**KeyRolloverStatusEnum**](#KeyRolloverStatusEnum) | The key rollover status which indicates if key rollover is required or not. If secrets encryption has been upgraded, then it requires key rollover. |  |



## Enum: EncryptionStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: KeyRolloverStatusEnum

| Name | Value |
|---- | -----|
| REQUIRED | &quot;Required&quot; |
| NOT_REQUIRED | &quot;NotRequired&quot; |



