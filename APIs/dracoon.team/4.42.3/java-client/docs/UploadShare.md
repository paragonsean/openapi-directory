

# UploadShare

Upload Share information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessKey** | **String** | Share access key to generate secure link |  |
|**cntFiles** | **Integer** | Total amount of existing files uploaded with this share. |  [optional] |
|**cntUploads** | **Integer** | Total amount of uploads conducted with this share. |  [optional] |
|**createdAt** | **OffsetDateTime** | Creation date |  |
|**createdBy** | [**UserInfo**](UserInfo.md) |  |  |
|**dataUrl** | **String** | Upload Share URL |  [optional] |
|**expireAt** | **OffsetDateTime** | Expiration date |  [optional] |
|**filesExpiryPeriod** | **Integer** | Number of days after which uploaded files expire |  [optional] |
|**id** | **Long** | Share ID |  |
|**internalNotes** | **String** | &amp;#128640; Since v4.11.0  Internal notes |  [optional] |
|**isEncrypted** | **Boolean** | Encryption state |  [optional] |
|**isProtected** | **Boolean** | Is share protected by password |  |
|**maxSize** | **Long** | Maximal total size of uploaded files (in bytes) |  [optional] |
|**maxSlots** | **Integer** | Maximal amount of files to upload |  [optional] |
|**name** | **String** | Alias name |  |
|**notes** | **String** | User notes |  [optional] |
|**notifyCreator** | **Boolean** | &amp;#128679; Deprecated since v4.20.0  Notify creator on every upload. |  |
|**recipients** | **String** | &amp;#128679; Deprecated since v4.11.0  CSV string of recipient email addresses |  [optional] |
|**showCreatorName** | **Boolean** | &amp;#128640; Since v4.11.0  Show creator first and last name. |  [optional] |
|**showCreatorUsername** | **Boolean** | &amp;#128640; Since v4.11.0  Show creator email address. |  [optional] |
|**showUploadedFiles** | **Boolean** | Allow display of already uploaded files |  [optional] |
|**smsRecipients** | **String** | &amp;#128679; Deprecated since v4.11.0  CSV string of recipient MSISDNs |  [optional] |
|**targetId** | **Long** | Target room or folder ID |  |
|**targetPath** | **String** | Path to shared upload node |  [optional] |
|**targetType** | **String** | Node type |  [optional] |
|**updatedAt** | **OffsetDateTime** | Modification date |  [optional] |
|**updatedBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |



