

# ImageStoreCopyDescription

Information about how to copy image store content from one image store relative path to another image store relative path.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkMarkFile** | **Boolean** | Indicates whether to check mark file during copying. The property is true if checking mark file is required, false otherwise. The mark file is used to check whether the folder is well constructed. If the property is true and mark file does not exist, the copy is skipped. |  [optional] |
|**remoteDestination** | **String** | The relative path of destination image store content to be copied to. |  |
|**remoteSource** | **String** | The relative path of source image store content to be copied from. |  |
|**skipFiles** | **List&lt;String&gt;** | The list of the file names to be skipped for copying. |  [optional] |



