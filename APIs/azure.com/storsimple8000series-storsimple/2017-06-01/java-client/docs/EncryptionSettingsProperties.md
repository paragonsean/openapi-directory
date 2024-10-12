

# EncryptionSettingsProperties

The properties of encryption settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionStatus** | [**EncryptionStatusEnum**](#EncryptionStatusEnum) | The encryption status to indicates if encryption is enabled or not. |  |
|**keyRolloverStatus** | [**KeyRolloverStatusEnum**](#KeyRolloverStatusEnum) | The key rollover status to indicates if key rollover is required or not. If secret&#39;s encryption has been upgraded, then it requires key rollover. |  |



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



