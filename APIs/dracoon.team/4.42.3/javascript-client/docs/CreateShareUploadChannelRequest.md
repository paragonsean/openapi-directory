# DracoonApi.CreateShareUploadChannelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directS3Upload** | **Boolean** | &amp;#128640; Since v4.15.0  Upload direct to S3 | [optional] [default to false]
**name** | **String** | File name | 
**password** | **String** | Password | [optional] 
**size** | **Number** | File size in byte | [optional] 
**timestampCreation** | **Date** | &amp;#128640; Since v4.22.0  Time the node was created on external file system  (default: current server datetime in UTC format) | [optional] 
**timestampModification** | **Date** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system  (default: current server datetime in UTC format) | [optional] 


