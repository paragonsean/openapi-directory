# DracoonApi.UpdateFileRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **Number** | Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential | [optional] 
**expiration** | [**ObjectExpiration**](ObjectExpiration.md) |  | [optional] 
**name** | **String** | File name | [optional] 
**notes** | **String** | User notes  Use empty string to remove. | [optional] 
**timestampCreation** | **Date** | &amp;#128640; Since v4.22.0  Time the node was created on external file system  (default: current server datetime in UTC format) | [optional] 
**timestampModification** | **Date** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system  (default: current server datetime in UTC format) | [optional] 


