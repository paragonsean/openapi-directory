

# BackupProperties

Class represents Backup properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **OffsetDateTime** | The time when the backup was created. |  [optional] |
|**deviceId** | **String** | The Device Identifier. |  |
|**elements** | [**List&lt;BackupElement&gt;**](BackupElement.md) | The backup elements. |  |
|**expirationTime** | **OffsetDateTime** | The time when the backup will expire. |  [optional] |
|**initiatedBy** | [**InitiatedByEnum**](#InitiatedByEnum) | Indicates how the backup was initiated \&quot;Manual | Scheduled\&quot;. |  |
|**sizeInBytes** | **Long** | The backup size in bytes. |  |
|**targetId** | **String** | The path id of the target FileServer or IscsiServer for which the backup was taken. |  [optional] |
|**targetType** | **String** | Type of target, FileServer or IscsiServer |  [optional] |



## Enum: InitiatedByEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;Manual&quot; |
| SCHEDULED | &quot;Scheduled&quot; |



