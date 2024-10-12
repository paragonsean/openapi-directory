

# Share

A Filestore share.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backup** | **String** | Immutable. Full name of the Cloud Filestore Backup resource that this Share is restored from, in the format of projects/{project_id}/locations/{location_id}/backups/{backup_id}. Empty, if the Share is created from scratch and not restored from a backup. |  [optional] |
|**capacityGb** | **String** | File share capacity in gigabytes (GB). Filestore defines 1 GB as 1024^3 bytes. Must be greater than 0. |  [optional] |
|**createTime** | **String** | Output only. The time when the share was created. |  [optional] [readonly] |
|**description** | **String** | A description of the share with 2048 characters or less. Requests with longer descriptions will be rejected. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Resource labels to represent user provided metadata. |  [optional] |
|**mountName** | **String** | The mount name of the share. Must be 63 characters or less and consist of uppercase or lowercase letters, numbers, and underscores. |  [optional] |
|**name** | **String** | Output only. The resource name of the share, in the format &#x60;projects/{project_id}/locations/{location_id}/instances/{instance_id}/shares/{share_id}&#x60;. |  [optional] [readonly] |
|**nfsExportOptions** | [**List&lt;NfsExportOptions&gt;**](NfsExportOptions.md) | Nfs Export Options. There is a limit of 10 export options per file share. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The share state. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| DELETING | &quot;DELETING&quot; |



