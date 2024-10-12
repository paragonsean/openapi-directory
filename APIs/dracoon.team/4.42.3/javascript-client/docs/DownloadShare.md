# DracoonApi.DownloadShare

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessKey** | **String** | Share access key to generate secure link | 
**classification** | **Number** | &amp;#128679; Deprecated since v4.11.0  Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    (default: classification from parent room) | [optional] 
**cntDownloads** | **Number** | Downloads counter (incremented on each download) | 
**createdAt** | **Date** | Creation date | 
**createdBy** | [**UserInfo**](UserInfo.md) |  | 
**dataUrl** | **String** | Path to shared download node | [optional] 
**expireAt** | **Date** | Expiration date | [optional] 
**id** | **Number** | Share ID | 
**internalNotes** | **String** | &amp;#128640; Since v4.11.0  Internal notes | [optional] 
**isEncrypted** | **Boolean** | Encrypted share  (this only applies to shared files, not folders) | [optional] 
**isProtected** | **Boolean** | Is share protected by password | [optional] 
**maxDownloads** | **Number** | Max allowed downloads | [optional] 
**name** | **String** | Alias name | 
**nodeId** | **Number** | Source node ID | 
**nodePath** | **String** | Path to shared download node | [optional] 
**nodeType** | **String** | Node type | [optional] 
**notes** | **String** | User notes | [optional] 
**notifyCreator** | **Boolean** | &amp;#128679; Deprecated since v4.20.0  Notify creator on every download. | 
**recipients** | **String** | &amp;#128679; Deprecated since v4.11.0  CSV string of recipient email addresses | [optional] 
**showCreatorName** | **Boolean** | Show creator first and last name. | [optional] 
**showCreatorUsername** | **Boolean** | Show creator email address. | [optional] 
**smsRecipients** | **String** | &amp;#128679; Deprecated since v4.11.0  CSV string of recipient MSISDNs | [optional] 
**updatedAt** | **Date** | Modification date | [optional] 
**updatedBy** | [**UserInfo**](UserInfo.md) |  | [optional] 



## Enum: ClassificationEnum


* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)




