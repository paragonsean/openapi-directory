

# ClassAttachmentCreation

Attachment creation for an assignment or stream post. This attachment must contain a `score` or an `url`, all the details of this one will be resolved and returned as `ClassAttachment` once the assignment or stream post is created. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**googleDriveFileId** | **String** | The ID of the Google Drive File |  [optional] |
|**lockScoreTemplate** | **Boolean** | To be used with a score attached in &#x60;sharingMode&#x60; &#x60;copy&#x60; (score used as template). If true, students won&#39;t be able to change the original notes of the template. |  [optional] |
|**score** | **String** | A unique Flat score identifier. The user creating the assignment must at least have read access to the document. If the user has admin rights, new group permissions will be automatically added for the teachers and students of the class.  |  [optional] |
|**sharingMode** | **MediaScoreSharingMode** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the attachment posted |  [optional] |
|**url** | **String** | The URL of the attachment. |  [optional] |
|**worksheet** | **String** | An unique worksheet identifier |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FLAT | &quot;flat&quot; |
| LINK | &quot;link&quot; |
| GOOGLE_DRIVE | &quot;googleDrive&quot; |
| WORKSHEET | &quot;worksheet&quot; |



