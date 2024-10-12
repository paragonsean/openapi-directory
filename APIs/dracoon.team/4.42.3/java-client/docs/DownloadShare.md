

# DownloadShare

Download Share information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessKey** | **String** | Share access key to generate secure link |  |
|**classification** | [**ClassificationEnum**](#ClassificationEnum) | &amp;#128679; Deprecated since v4.11.0  Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    (default: classification from parent room) |  [optional] |
|**cntDownloads** | **Integer** | Downloads counter (incremented on each download) |  |
|**createdAt** | **OffsetDateTime** | Creation date |  |
|**createdBy** | [**UserInfo**](UserInfo.md) |  |  |
|**dataUrl** | **String** | Path to shared download node |  [optional] |
|**expireAt** | **OffsetDateTime** | Expiration date |  [optional] |
|**id** | **Long** | Share ID |  |
|**internalNotes** | **String** | &amp;#128640; Since v4.11.0  Internal notes |  [optional] |
|**isEncrypted** | **Boolean** | Encrypted share  (this only applies to shared files, not folders) |  [optional] |
|**isProtected** | **Boolean** | Is share protected by password |  [optional] |
|**maxDownloads** | **Integer** | Max allowed downloads |  [optional] |
|**name** | **String** | Alias name |  |
|**nodeId** | **Long** | Source node ID |  |
|**nodePath** | **String** | Path to shared download node |  [optional] |
|**nodeType** | **String** | Node type |  [optional] |
|**notes** | **String** | User notes |  [optional] |
|**notifyCreator** | **Boolean** | &amp;#128679; Deprecated since v4.20.0  Notify creator on every download. |  |
|**recipients** | **String** | &amp;#128679; Deprecated since v4.11.0  CSV string of recipient email addresses |  [optional] |
|**showCreatorName** | **Boolean** | Show creator first and last name. |  [optional] |
|**showCreatorUsername** | **Boolean** | Show creator email address. |  [optional] |
|**smsRecipients** | **String** | &amp;#128679; Deprecated since v4.11.0  CSV string of recipient MSISDNs |  [optional] |
|**updatedAt** | **OffsetDateTime** | Modification date |  [optional] |
|**updatedBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |



## Enum: ClassificationEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |



